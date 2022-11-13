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
                    num = random.randrange(1, maxNum + 1)  # Randomly selects a joke in the database

                    jokes = cur.execute("SELECT content FROM JOKE WHERE number = ?", (num,))
                    for joke in jokes:
                        conn.send(joke[0].encode(FORMAT))
        elif command == "QUIT":
                connect = False

    print(str(addr) + " : QUIT")
    conn.close()




    #elif command == "INSERT":

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
