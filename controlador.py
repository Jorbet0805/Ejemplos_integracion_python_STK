from win32api import GetSystemMetrics
import comtypes

# Start new instance of STK
from comtypes.client import CreateObject
from comtypes.gen import STKUtil
from comtypes.gen import STKObjects

import os
import pdb
from datetime import datetime
from datetime import timedelta

import integracion_stk_modificar_fecha as istk
import util.busqueda_eph as busqueda_eph
import util.mensaje_error as mensaje_error
import util.getdirsandfiles as getdirsandfiles
import util.control_error_decoradores as decorador


class appstk():
    def __init__(self):

        self.uiApplication = None
        self.type = None
        self.path_sc = None
        self.root_actual = None
        
    def get_cliente(self, 
                    type="cargar",
                    visible=False
                    ):

        if self.uiApplication != None:
            print("Ya existe un cliente")
            return

        self.type = type
        
        print("creando interfaz")

        if self.type == "crear" or self.type == "cargar":
            print("creando o cargando")
            import pythoncom
            pythoncom.CoInitialize()
            self.uiApplication = CreateObject('STK10.Application')
        
        if self.type == "enganchar":
            import pythoncom
            pythoncom.CoInitialize()
            print("engancandose")
            self.uiApplication = comtypes.client.GetActiveObject('STK10.Application')

        if visible: 
            print("haciendo visible")
        self.uiApplication.Visible=visible
        print("Hecho visible")

       
    def getroot(self,path_sc=None):

        self.path_sc = path_sc

        if self.uiApplication == None:
            print("Debe de crear un cliente primero")
            return None

        import pythoncom
        pythoncom.CoInitialize()
        cliente_stk = self.uiApplication
        root = cliente_stk.Personality2

        if self.type == "cargar":
           #Cargar scenario
           print("cargando archivo: ".format(self.path_sc))
           root.LoadScenario( self.path_sc)

        self.root_actual = root   

        return root

    def delcliente(self):
        try:
           del self.uiApplication
           self.uiApplication = None
        except:
            pass



@decorador.decorador_error(mensaje="Error en actualizar fecha",
                 hacer_print=True,
                 mensaje_comienzo="Actualizando Fechas"
                 )
def actualizar_fecha(root,tiempo_incial,tiempo_final):

    actualizadorfecha = istk.actualizarfecha(root)
    actualizadorfecha.updatefecha(tiempo_incial,tiempo_final)
    
    
@decorador.decorador_error(mensaje="Error en guardar escenario",
                 hacer_print=True,
                 mensaje_comienzo="Guardando escenario"
                 )
def guardar_escenario(root):
    guardador = istk.guardador(root)
    guardador.guardar_escenario()


def procesar_escenarios(
        boton,
        directorio_escenarios, 
        tiempo_incial,
        tiempo_final, 
        act_tiempo,
        visible
        ):

    try:
    
        if boton:
           label_inicial = boton.GetLabel()
           boton.Disable() 

        buscador = getdirsandfiles.get_dirs_files()

        subdirectorios = buscador.get_dirs(directorio_escenarios) 
        #print(subdirectorios)

        subdirectorio = subdirectorios[0]
        subdirectorio = os.path.join(directorio_escenarios,subdirectorio)
        fichero_sc = buscador.get_file_ext(subdirectorio)
        #print(fichero_sc)

        ficheros_sc = buscador.get_files_ext(subdirectorios, ext='.sc')
        #print(ficheros_sc)

        app = appstk()

        #crear directorio para guardar reportes
        try:
            os.makedirs(os.path.join(directorio_escenarios,"reportes"))
            path_dir_reportes = os.path.join(directorio_escenarios,"reportes")
        except:
            path_dir_reportes = os.path.join(directorio_escenarios,"reportes")


        iter = 0
        for fichero_sc in ficheros_sc:
            print(fichero_sc)

            type = "cargar"
        
            if boton:
               boton.SetLabel( "Procesando {0}".format(iter) )


            app.get_cliente(
                            type=type,
                            visible=visible
                            )
            root = app.getroot(path_sc=fichero_sc)

        
            if act_tiempo: 
               actualizar_fecha(root,tiempo_incial,tiempo_final)
            
            guardar_escenario(root)
            iter += 1
    
        app.delcliente()
        print("Proceso finalizado")

        if  boton:
            boton.SetLabel(label_inicial)
            boton.Enable()
    except:
        print("Proceso interrumpido")
        app.delcliente()
        if  boton:
            boton.SetLabel(label_inicial)
            boton.Enable()


if __name__ == "__main__":
   
    deltat = 7
    now = datetime.now()

    StardPlan = now + timedelta(days=2)
    StartTime = StardPlan.strftime('%d %b %Y 00:00:00.00')
   
    EndPlan = now + timedelta( days= deltat + 2 )
    EndTime = EndPlan.strftime('%d %b %Y 00:00:00.00')
    
    directorio_escenarios = "D:\\Mis documentos\\Jorge\\ABAE\\OMS\\Escenaros_2"
    directorio_EPH = 'C:\\Users\\BAJAME\\Anaconda3\\envs\\updatestkescenario\\mapp\\EPH'
    procesar_escenarios(
        boton=None,
        directorio_escenarios=directorio_escenarios, 
        tiempo_incial=StartTime,
        tiempo_final=EndTime, 
        directorio_EPH=directorio_EPH, 
        act_parametros_orbitales=False, 
        act_tiempo=True,
        crear_reporte_accesos=False, 
        visible=False
        )