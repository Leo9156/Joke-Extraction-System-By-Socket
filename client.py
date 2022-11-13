import wx
import wx.xrc
import socket

serverName = "127.0.0.1"
serverPort = 12000
FORMAT = 'utf-8'
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("client connects to the server")

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande" ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 100 )

        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Select", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

        gSizer1.Add( self.m_button2, 0, wx.ALL, 5 )


        bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizer1 )
        self.m_panel1.Layout()
        bSizer1.Fit( self.m_panel1 )
        self.m_notebook1.AddPage( self.m_panel1, u"Show", False )
        self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Insert a joke:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
        bSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( bSizer2 )
        self.m_panel2.Layout()
        bSizer2.Fit( self.m_panel2 )
        self.m_notebook1.AddPage( self.m_panel2, u"Insert", False )

        gbSizer1.Add( self.m_notebook1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( gbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.Select_From_Server )
        self.m_button2.Bind( wx.EVT_BUTTON, self.ExitGUI )
        self.m_button3.Bind( wx.EVT_BUTTON, self.Insert_to_Server )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Select_From_Server( self, event ):
        # send the request to the server
        command = "GET"
        clientSocket.send(command.encode(FORMAT))

        # receive the joke from the server
        joke = clientSocket.recv(2048).decode(FORMAT)
        
        if joke == "empty":
            self.m_staticText1.SetLabel("Empty!")

        self.m_staticText1.SetLabel(joke)

        # close the connection
        #clientSocket.close()

    def ExitGUI( self, event ):
        command = "QUIT"
        clientSocket.send(command.encode(FORMAT))
        #clientSocket.close()
        print("The connection is closed")
        self.Close(True)

    def Insert_to_Server( self, event ):
        # send the request to the server
        command = "INSERT"
        clientSocket.send(command.encode(FORMAT))

        # insert the joke to the server
        joke = self.m_textCtrl2.GetValue()
        print(type(joke))
        clientSocket.send(joke.encode(FORMAT))

if __name__ == "__main__":
    #clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #clientSocket.connect((serverName, serverPort))
    app = wx.App()
    frm = MyFrame2(None)
    frm.Show()
    app.MainLoop()