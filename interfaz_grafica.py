# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv as wxadv
from datetime import datetime
from datetime import timedelta
import pdb
from threading import Thread

import controlador


###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500, 400), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        
        self.SetSizer( self.bSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    

###########################################################################
## Class Panel_calendario
###########################################################################

class Panel_calendario ( wx.Panel ):
    
    def __init__( self, parent, hermano_textCtr ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(-1,-1), style = wx.TAB_TRAVERSAL )
        
        self.hermano_textCtr = hermano_textCtr
        self.parent = parent

        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_calendar2 = wxadv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize )
        bSizer13.Add( self.m_calendar2, 1, wx.ALL, 5 )
        
        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button86 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button86, 1, wx.ALL, 5 )
        
        self.m_button87 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button87, 1, wx.ALL, 5 )
        
        
        bSizer13.Add( bSizer14, 0, wx.ALL, 5 )
        
        
        self.SetSizer( bSizer13 )
        self.Layout()
        bSizer13.Fit( self )
        
        # Connect Events
        self.m_button86.Bind( wx.EVT_LEFT_DOWN, self.m_button86OnLeftDown )
        self.m_button87.Bind( wx.EVT_LEFT_DOWN, self.m_button87OnLeftDown )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_button86OnLeftDown( self, event ):
        tiempo = self.m_calendar2.GetDate()
        tiempo = tiempo.Format('%d %b %Y 00:00:00.00')
        tiempo = str(tiempo)
        #print(tiempo)
        self.hermano_textCtr.SetLabelText(tiempo)
        self.parent.Destroy() 
    

    def m_button87OnLeftDown( self, event ):
        self.parent.Destroy() 


def conseguir_tiempo_final(modo):
    if modo == 0:
        deltat = 7
    if modo == 1:
        deltat = 30
    if modo == 2:
        deltat = 30*3
    if modo == 3:
        deltat = 30*4

    now = datetime.now()
    EndPlan = now + timedelta( days= deltat + 2 )
    EndTime = EndPlan.strftime('%d %b %Y 00:00:00.00')
    return EndTime

def conseguir_tiempo_inicial(modo):
    now = datetime.now()
    StardPlan = now + timedelta(days=2)
    StartTime = StardPlan.strftime('%d %b %Y 00:00:00.00')
    return StartTime

###########################################################################
## Class Panel_eleguir_tiempo
###########################################################################

class Panel_eleguir_tiempo ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
        
        self.parent = parent

        bSizer17 = wx.BoxSizer( wx.VERTICAL )
        
        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Tiempo", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText18.Wrap( -1 )
        self.m_staticText18.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
        gbSizer3.Add( self.m_staticText18, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        #gbSizer3.AddSpacer( ( 250, 1 ), wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
        
        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Tiempo Inicial", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        self.m_staticText20.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
        gbSizer3.Add( self.m_staticText20, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Tiempo Final", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        self.m_staticText21.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
        gbSizer3.Add( self.m_staticText21, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        gbSizer3.Add( self.m_textCtrl7, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        comboBoxChoices = [ u"Semanal", u"Mensual", u"Trimestral", u"Cuatrimestral", u"Date" ]        
        self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Semanal", wx.DefaultPosition, wx.DefaultSize, comboBoxChoices, 0 )
        gbSizer3.Add( self.m_comboBox3, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,  wx.Size( 180,-1 ), 0 )
        gbSizer3.Add( self.m_textCtrl6, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        m_comboBox2Choices = [ u"Semanal", u"Mensual", u"Trimestral", u"Cuatrimestral", u"Date" ]
        self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Semanal", wx.DefaultPosition, wx.DefaultSize, comboBoxChoices, 0 )
        gbSizer3.Add( self.m_comboBox2, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer17.Add( gbSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.SHAPED, 5 )
    
        self.SetSizer( bSizer17 )
        self.Layout()
    
        # Connect Events
        self.m_comboBox2.Bind( wx.EVT_TEXT, self.m_comboBox2OnText )
        self.m_comboBox3.Bind( wx.EVT_TEXT, self.m_comboBox3OnText )
        # Connect Events
        self.m_textCtrl7.Bind( wx.EVT_TEXT, self.m_textCtrl7OnText )
        self.m_textCtrl6.Bind( wx.EVT_TEXT, self.m_textCtrl6OnText )
		
    
    def __del__( self ):
        pass
    
    
    
    def m_comboBox2OnText( self, event ):
        objeto = event.GetEventObject()
        texto_actual = objeto.GetStringSelection()
        seleccion_actual = objeto.GetCurrentSelection();
        if texto_actual == "Date":
            llamar_calendario(self.m_textCtrl6)
        if seleccion_actual in range(4):
            tiempo_inicial = conseguir_tiempo_inicial(seleccion_actual)
            tiempo_final = conseguir_tiempo_final(seleccion_actual)
            #print(tiempo_inicial,"-",tiempo_final)
            self.m_textCtrl7.SetLabelText(tiempo_final)
            self.m_textCtrl6.SetLabelText(tiempo_inicial)

    def m_comboBox3OnText( self, event ):
        objeto = event.GetEventObject()
        texto_actual = objeto.GetStringSelection()
        seleccion_actual = objeto.GetCurrentSelection();
        if texto_actual == "Date":
            llamar_calendario(self.m_textCtrl7)
        if seleccion_actual in range(4):
            tiempo_inicial = conseguir_tiempo_inicial(seleccion_actual)
            tiempo_final = conseguir_tiempo_final(seleccion_actual)
            #print(tiempo_inicial,"-",tiempo_final)
            self.m_textCtrl7.SetLabelText(tiempo_final)
            self.m_textCtrl6.SetLabelText(tiempo_inicial)

        
       # Virtual event handlers, overide them in your derived class
    def m_textCtrl7OnText( self, event ):
        event.Skip()
	
    def m_textCtrl6OnText( self, event ):
        event.Skip()
        
###########################################################################
## Class Panel_direscenario
###########################################################################

class Panel_direscenario ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1, -1 ), style = wx.TAB_TRAVERSAL )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Directorio escenario", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
        bSizer9.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer9.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer9 )
        self.Layout()
    
    def __del__( self ):
        pass

###########################################################################
## Class Panel_button
###########################################################################

class Panel_button ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
        
        self.parent = parent
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Presione para Procesar", wx.DefaultPosition,  wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
        bSizer15.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.SetSizer( bSizer15 )
        self.Layout()
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_LEFT_DOWN, self.m_button1OnLeftDown )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_button1OnLeftDown( self, event ):

        boton = event.GetEventObject()
        
        hijos = self.parent.GetChildren()
		
        Panel_direscenario = hijos[0]
        Panel_eleguir_tiempo = hijos[1]  
       
        directorio_escenarios = Panel_direscenario.m_dirPicker1.GetPath()
        
        tiempo_incial = Panel_eleguir_tiempo.m_textCtrl6.GetValue()
        tiempo_final = Panel_eleguir_tiempo.m_textCtrl7.GetValue()

        act_tiempo = True
        visible = True

        print(visible)
        print(tiempo_incial)
        print(tiempo_final)
        print(directorio_escenarios)

        #print(self.parent.Children.Panel_direscenario)

        hilo = Thread( 
                    target= controlador.procesar_escenarios,
                    kwargs={
                         "boton":boton,
                         "directorio_escenarios":directorio_escenarios, 
                         "tiempo_incial":tiempo_incial,
                         "tiempo_final":tiempo_final, 
                         "act_tiempo":act_tiempo,
                         "visible":visible},
                    daemon=False)    
        hilo.start()


def llamar_calendario(hermano_textCtr):
    Frame_calendario = Frame(parent=None)
    panel = Panel_calendario(parent=Frame_calendario, hermano_textCtr=hermano_textCtr)
    Frame_calendario.bSizer3.Add( panel, 1, wx.EXPAND |wx.ALL, 5 )
    Frame_calendario.Show(True)

    #app.MainLoop() 


if __name__ == '__main__':
    
    try:
        del app
        app = wx.App()
    except:
        app = wx.App() 
     
    Frame_principal = Frame(parent=None)

    Sizer_panel_principal = Frame_principal.bSizer3

    Panel_direscenario = Panel_direscenario(parent=Frame_principal)
    Sizer_panel_principal.Add( Panel_direscenario, 1, wx.EXPAND|wx.ALL, 5 )

    Panel_eleguir_tiempo = Panel_eleguir_tiempo(parent=Frame_principal)
    Sizer_panel_principal.Add( Panel_eleguir_tiempo, 1, wx.EXPAND|wx.ALL, 5 )

    Panel_button = Panel_button(parent=Frame_principal)
    Sizer_panel_principal.Add( Panel_button, 1, wx.EXPAND|wx.ALL, 5 )

    Frame_principal.Show(True)

    app.MainLoop() 