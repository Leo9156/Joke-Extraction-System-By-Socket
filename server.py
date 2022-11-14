import socket
import sqlite3
import threading
import random

ADDR = ('127.0.0.1', 12000)
FORMAT = 'utf-8'

def handle_client(conn, addr):
    print("[NEW CONNECTION] The client " + str(addr) + " is connected.")

    connect = True
    while connect:
        command = conn.recv(1024).decode(FORMAT)
        
        # connect to the database
        con = sqlite3.connect("//Users//leoyang//Desktop//大三//計算機網路//socket_programming//TCP//jokeDB.db")
        cur = con.cursor()

        if command == "GET":
            print(str(addr) + " : GET")

            rows = cur.execute("SELECT MAX(number) FROM JOKE ")
            for row in rows:
                if row[0] == None:
                    conn.send("empty".encode(FORMAT))
                else:
                    maxNum = row[0]
                    num = random.randrange(1, maxNum + 1)  # Randomly selects a joke in the database according to the number field

                    jokes = cur.execute("SELECT content FROM JOKE WHERE number = ?", (num,))
                    for joke in jokes:
                        conn.send(joke[0].encode(FORMAT))
        elif command == "QUIT":
                connect = False

        elif command == "INSERT":
            print(str(addr) + " : INSERT")
            conn.send("OK".encode(FORMAT))  # response to the client

            inputJoke = conn.recv(2048).decode(FORMAT) # get the joke from the client
            
            #Insert the joke into the database
            rows = cur.execute("SELECT MAX(number) FROM JOKE ")
            for row in rows:
                if row[0] == None:
                    number = 0
                else:
                    number = row[0]

            cur.execute("INSERT INTO JOKE VALUES (?, ?)", (number + 1, inputJoke))
            con.commit()

    con.close()
    print(str(addr) + " : QUIT")
    conn.close()

    #else:


def main():
    # create a server socket and bind it to the ADDR
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(ADDR)
    serverSocket.listen(5)
    print("[STARTING] The server is ready...")

    while True:
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))  # multithreading
        thread.start()
        print("[ACTIVE CONNECTIONS] " + str(threading.active_count() - 1))

if __name__ == '__main__':
    main()
