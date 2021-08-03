#!/usr/bin/env python
# coding: utf-8

from win32api import GetSystemMetrics
import comtypes

# Start new instance of STK
#from comtypes.client import CreateObject
#uiApplication = CreateObject('STK10.Application')
#uiApplication.Visible = True


# Alternatively, uncomment the following lines to get a reference to a running STK instance
from comtypes.client import GetActiveObject

from comtypes.gen import STKUtil
from comtypes.gen import STKObjects

from datetime import datetime
from datetime import timedelta
from lxml import etree
import pandas as pd
import numpy as np
import os

import pdb


#import sys
#print(sys.executable)


path_file_eph = os.path.join(os.path.dirname(__file__), "EPH\\OMS_TDRS_VRSS-2_20210107_000000002071.EPH");

def formatear_OrbitEpoch(OrbitEpoch):
        OrbitEpoch = OrbitEpoch.replace('T',' ');
        OrbitEpoch_datatime = datetime.strptime(OrbitEpoch, '%Y-%m-%d %H:%M:%S');
        OrbitEpoch = OrbitEpoch_datatime.strftime('%d %b %Y %H:%M:%S');
        return OrbitEpoch
        

class actualizarfecha():
    def __init__(self,root):
        self.root = root

    def getIescenario(self):
        self.Iescenario = self.root.CurrentScenario.QueryInterface(STKObjects.IAgScenario)
        return self.Iescenario

    def updatefecha(self,StartTime,EndTime):

        #pdb.set_trace() 
        print("Actualizando fecha: ",StartTime,"-",EndTime )     
        self.getIescenario()
        try:
            self.Iescenario.SetTimePeriod (StartTime,EndTime)
            self.Iescenario.StartTime = str(StartTime)
        except:
            self.Iescenario.StartTime = str(StartTime)
            self.Iescenario.StopTime = str(EndTime)         


class guardador():
    def __init__(self,root):
        self.root = root
    def guardar_escenario(self):
        self.root.SaveScenario()
        self.root.CloseScenario(); 


if __name__ == '__main__':
   #Insetar rejilla
   uiApplication=GetActiveObject('STK10.Application')
   uiApplication.Visible=True

   #Note: When 'root=uiApplication.Personality2' is executed, the comtypes library automatically creates a gen folder that contains STKUtil and STK Objects. After running this at least once on your computer, the following two lines should be moved before the 'uiApplication=CreateObject("STK11.Application")' line for improved performance.    
   root=uiApplication.Personality2

   Iescenario = root.CurrentScenario.QueryInterface(STKObjects.IAgScenario)


   #path_rejilla= os.path.join(os.path.dirname(__file__), "Rejilla.csv");
   #creadorderejilla=creartarjetrejilla(root,path_rejilla);
   #creadorderejilla.insertartajets();
   
   #del uiApplication
   
   #Actualizar parametros orbitales
   #file_eph = 'F:\\Usuario\\Desktop\\EPH\\OMS_TDRS_VRSS-2_20210107_000000002071.EPH';
   #manejadorstk = actualizarparaorbitales(root,file_eph);
   #n_satelite = 2;
   #manejadorstk.satupdateparam(n_satelite);


   #Actualizar fecha
   #file_eph = 'F:\\Usuario\\Desktop\\EPH\\OMS_TDRS_VRSS-2_20210107_000000002071.EPH';  
   #manejadorstk = actualizarparaorbitales(root,file_eph);
   #manejadorstk.updatefecha()

   #creadorreporte = creador_reporte(root)
   #reporte = creadorreporte.crear_reporte()
   #creadorreporte.guardar_reporte()
   #print(reporte)

   path_guardado_provi = 'C:\\Users\\BAJAME\\Documents\\Favorites\\elimpf_instrucc\\Desktop\\Simulaciones'


   #path_logo = os.path.join(os.path.dirname(__file__), "ABAE_logo.png") 