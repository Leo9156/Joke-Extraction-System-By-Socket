import wx
import wx.xrc
import socket
import re

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

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,175 ), 0)
        self.m_staticText1.Wrap(100)

        bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )

        gSizer2 = wx.GridSizer( 0, 2, 0, 250 )

        self.m_button1 = wx.Button( self.m_panel3, wx.ID_ANY, u"select", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, u"exit", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


        bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        self.m_notebook2.AddPage( self.m_panel3, u"select", False )
        self.m_panel4 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Insert a joke:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,125 ), style=wx.TE_MULTILINE)
        bSizer5.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self.m_panel4, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button3, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        self.m_notebook2.AddPage( self.m_panel4, u"insert", False )

        bSizer3.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer3 )
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
        joke = re.sub(r"(.{35})", "\\1\r\n", joke)  # append a new line every 35 chracters
        
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
        # insert the joke to the server
        joke = self.m_textCtrl2.GetValue()

        if len(joke) == 0:
            self.m_staticText5.SetLabel("WARNING: Insertion cannot be empty!")
        elif len(joke) > 500:
            self.m_staticText5.SetLabel("WARNING: Cannot insert over 500 letters!")
        else:
            self.m_staticText5.SetLabel("")
            # send the request to the server
            command = "INSERT"
            clientSocket.send(command.encode(FORMAT))
            response = clientSocket.recv(1024).decode(FORMAT)
            if response == "OK":
                clientSocket.send(joke.encode(FORMAT))
            #clientSocket.send(joke.encode(FORMAT))

if __name__ == "__main__":
    #clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #clientSocket.connect((serverName, serverPort))
    app = wx.App()
    frm = MyFrame2(None)
    frm.Show()
    app.MainLoop()