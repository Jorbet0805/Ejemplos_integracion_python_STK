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

import integracion_stk as istk
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
                    type="crear",
                    visible=False
                    ):

        if self.uiApplication != None:
            print("Ya existe un cliente")
            return

        self.type = type
        
        print("creando interfaz")

        if self.type == "crear":
            print("creando App")
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
        else:
            self.uiApplication.Visible=visible
            print("Hecho no visible")

        
    def getroot(self):
    
        if self.uiApplication == None:
            print("Debe de crear un cliente primero")
            return None
        
        import pythoncom
        pythoncom.CoInitialize()
        cliente_stk = self.uiApplication
        root = cliente_stk.Personality2

        self.root_actual = root 

        return root 
    
    def cargar_escenario (self,path_sc=None):
        
        self.path_sc = path_sc

        if self.root_actual == None:
           print("No hay nigun root definido")
           return

        if self.type == "cargar":
           #Cargar scenario
           print("cargando archivo: {0}".format(self.path_sc))
           self.root_actual.LoadScenario(self.path_sc)
        
        return self.root_actual 

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


@decorador.decorador_error(mensaje="A ocurrido un error en la insercion de objetivos",
                 hacer_print=True,
                 mensaje_comienzo="insertando objetivos"
                 )
def Insetar_objetivos (root,path_objetivos):
    #Insetar rejilla
 
        creadorderejilla=istk.introductor_objetivo(root,path_objetivos);
        creadorderejilla.insertartajets();
    
    
    
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
        dir_archivo_objetivos,
        tiempo_incial,
        tiempo_final,
        usar_escenario_activo, 
        act_tiempo,
        introducir_rejilla,
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


        iter = 0
        for fichero_sc in ficheros_sc:
            print(fichero_sc)
            
            if iter == 0:
                type = "crear"
                app.get_cliente(
                            type=type,
                            visible=visible
                            )
                app.getroot()
                root = app.root_actual
           
            
            app.type = "cargar" 
        
            if boton:
                boton.SetLabel( "Procesando {0}".format(iter) )
            
            app.cargar_escenario(path_sc=fichero_sc)

        
            if act_tiempo: 
               actualizar_fecha(root,tiempo_incial,tiempo_final)
            
            if introducir_rejilla:
               Insetar_objetivos (root,dir_archivo_objetivos)
            
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
    procesar_escenarios(
        boton=None,
        directorio_escenarios=directorio_escenarios, 
        tiempo_incial=StartTime,
        tiempo_final=EndTime, 
        act_tiempo=True,
        crear_reporte_accesos=False, 
        visible=False
        )