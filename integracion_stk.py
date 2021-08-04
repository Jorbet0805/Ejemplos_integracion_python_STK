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



class introductor_objetivo():
    def __init__(self,root,path_objetivos):
        self.root = root
        
        self.df = pd.read_csv(path_objetivos, header=0);
        
    def insertar_tarjet (self,nombre,latitud,longitud):
            
            if self.root.CurrentScenario.Children.Contains(STKObjects.eTarget,"{0}".format(nombre)):
                tarjet = self.root.CurrentScenario.Children.Item("{0}".format(nombre)) 
                #print(":tarjet {0} ya existe".format(nombre))
            else:
                tarjet = self.root.CurrentScenario.Children.New(STKObjects.eTarget,"{0}".format(nombre))
                #print(":tarjet {0} creado".format(nombre))
            
            tarjet2 = tarjet.QueryInterface(STKObjects.IAgTarget);
            tarjet2.Position.AssignPlanetodetic(float(latitud),float(longitud),0);
            tarjet2.Graphics.Color = 255
            tarjet2.Graphics.MarkerColor = 255
            
            return tarjet


        
    def insertartajets(self):
            
            for n_dato_objetivo in range(len(self.df)):
                
                datos_objetivo = self.df.iloc[n_dato_objetivo];

                nombre = datos_objetivo[0];
                latitud = datos_objetivo[1];
                longitud = datos_objetivo[2];
                
                target = self.insertar_tarjet (nombre,latitud,longitud);
    


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

   path_guardado_provi = 'C:\\Users\\BAJAME\\Documents\\Favorites\\elimpf_instrucc\\Desktop\\Simulaciones'
