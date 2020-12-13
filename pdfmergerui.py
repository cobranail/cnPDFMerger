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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF Merger", pos = wx.DefaultPosition, size = wx.Size( 437,304 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"File 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer2.Add( self.m_filePicker1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Reverse", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"File 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer3.Add( self.m_filePicker2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Reverse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		bSizer3.Add( self.m_checkBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox1Choices = [ u"Odd-Even", u"Append" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"Merge Mode", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer4.Add( self.m_radioBox1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker3 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		bSizer5.Add( self.m_filePicker3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mGuess = wx.Button( self, wx.ID_ANY, u"SameWithFile1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.mGuess, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )


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


