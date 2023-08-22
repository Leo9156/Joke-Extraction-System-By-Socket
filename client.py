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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 718,483 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,250 ), 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

        m_choice2Choices = [ u"諧音梗", u"地獄梗", u"猜謎", u"冷笑話", u"色情", wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString ]
        self.m_choice2 = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer5.Add( self.m_choice2, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Score", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer7.Add( self.m_staticText9, 0, wx.ALL, 5 )

        m_choice4Choices = [ u"1", u"2", u"3", u"4", u"5" ]
        self.m_choice4 = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        bSizer7.Add( self.m_choice4, 0, wx.ALL, 5 )

        self.m_button9 = wx.Button( self.m_panel3, wx.ID_ANY, u"submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button9, 0, wx.ALL, 5 )

        bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

        gSizer5 = wx.GridSizer( 0, 2, 0, 400 )

        self.m_button1 = wx.Button( self.m_panel3, wx.ID_ANY, u"select", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, u"exit", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button2, 0, wx.ALL, 5 )


        bSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        self.m_notebook2.AddPage( self.m_panel3, u"select", True )
        self.m_panel4 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Insert a joke:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer8.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer8.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,250 ), style=wx.TE_MULTILINE)
        bSizer8.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText12 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        bSizer9.Add( self.m_staticText12, 0, wx.ALL, 5 )

        m_choice5Choices = [ u"諧音梗", u"地獄梗", u"猜謎", u"冷笑話", u"色情", wx.EmptyString ]
        self.m_choice5 = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
        self.m_choice5.SetSelection( 0 )
        bSizer9.Add( self.m_choice5, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self.m_panel4, wx.ID_ANY, u"insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button3, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer8 )
        self.m_panel4.Layout()
        bSizer8.Fit( self.m_panel4 )
        self.m_notebook2.AddPage( self.m_panel4, u"insert", False )

        bSizer3.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button9.Bind( wx.EVT_BUTTON, self.SubmitScore )
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
        response = clientSocket.recv(1024).decode()

        if response == "OK":
            tag = self.m_choice2.GetStringSelection()
            clientSocket.send(tag.encode(FORMAT))

            joke = clientSocket.recv(2048).decode(FORMAT)

            if joke == "empty":
                    self.m_staticText1.SetLabel("Empty!")
                    self.m_staticText13.SetLabel("尚無評價!")
            else:
                clientSocket.send("RECEIVE".encode(FORMAT))
                num = clientSocket.recv(1024).decode(FORMAT)
                self.m_staticText13.SetLabel("評分: " + num)

                joke = re.sub(r"(.{50})", "\\1\r\n", joke)  # append a new line every 50 chracters
                self.m_staticText1.SetLabel(joke)

        else:
            print("The request of selection is turned down!")
            self.m_staticText1.SetLabel("The server didn't accept your request. Please try again!")

    def SubmitScore( self, event ):
        command = "SCORE"
        clientSocket.send(command.encode(FORMAT))
        response = clientSocket.recv(1024).decode(FORMAT)

        if response == "OK":
            score = self.m_choice4.GetStringSelection()
            clientSocket.send(score.encode(FORMAT))

    def ExitGUI( self, event ):
        command = "QUIT"
        clientSocket.send(command.encode(FORMAT))
        #clientSocket.close()
        print("The connection is closed")
        self.Close(True)

    def Insert_to_Server( self, event ):
        # insert the joke to the server
        joke = self.m_textCtrl2.GetValue()
        tag = self.m_choice5.GetStringSelection()

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
                receieve = clientSocket.recv(1024).decode(FORMAT)
                if receieve == "ACK":
                    clientSocket.send(tag.encode(FORMAT))
                else:
                    print("The server didn't receieve your insertion. Please try again!")
            else:
                print("The insertion request is turned down!")
                self.m_staticText5.SetLabel("The server rejects your insertion command. Please try again!")

if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame2(None)
    frm.Show()
    app.MainLoop()