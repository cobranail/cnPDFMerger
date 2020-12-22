# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF Merger", pos = wx.DefaultPosition, size = wx.Size( 589,304 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_listbook1 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel1 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"File 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer2.Add( self.m_filePicker1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Reverse", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer7.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"File 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer3.Add( self.m_filePicker2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Reverse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		bSizer3.Add( self.m_checkBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer7.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox1Choices = [ u"Odd-Even", u"Append" ]
		self.m_radioBox1 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Merge Mode", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer4.Add( self.m_radioBox1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker3 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		bSizer5.Add( self.m_filePicker3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mGuess = wx.Button( self.m_panel1, wx.ID_ANY, u"SameWithFile1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.mGuess, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer7.Add( bSizer5, 0, wx.EXPAND, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( bSizer6, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer7 )
		self.m_panel1.Layout()
		bSizer7.Fit( self.m_panel1 )
		self.m_listbook1.AddPage( self.m_panel1, u"Merger", False )
		self.m_panel2 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer9.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker4 = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer9.Add( self.m_filePicker4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer13.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer11.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_dirPicker2 = wx.DirPickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer11.Add( self.m_dirPicker2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Basename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer11.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = [ u"01", u"001", u"0001", u"00001" ]
		self.m_choice1 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer11.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer11, 1, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"Guess", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox3Choices = [ u"Each", u"Odd-Even" ]
		self.m_radioBox3 = wx.RadioBox( self.m_panel2, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 0 )
		bSizer15.Add( self.m_radioBox3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer15, 0, wx.EXPAND, 5 )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self.m_panel2, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer14, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer8 )
		self.m_panel2.Layout()
		bSizer8.Fit( self.m_panel2 )
		self.m_listbook1.AddPage( self.m_panel2, u"Spliter", False )

		bSizer1.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.mGuess.Bind( wx.EVT_BUTTON, self.guessname )
		self.m_button2.Bind( wx.EVT_BUTTON, self.export )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def guessname( self, event ):
		event.Skip()

	def export( self, event ):
		event.Skip()


