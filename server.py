import socket
import sqlite3
import threading

ADDR = ('127.0.0.1', 12000)
FORMAT = 'utf-8'

def handle_client(conn, addr):
    print("[NEW CONNECTION] The client " + str(addr) + " is connected.")

    num = -1

    connect = True
    while connect:
        command = conn.recv(1024).decode(FORMAT)
        
        # connect to the database
        con = sqlite3.connect("//Users//leoyang//Desktop//大三//計算機網路//socket_programming//TCP//jokeDB.db")
        cur = con.cursor()

        if command == "GET":
            print(str(addr) + " : GET")
            conn.send("OK".encode(FORMAT))

            tag = conn.recv(1024).decode(FORMAT)
            
            check = True
            rows = cur.execute("SELECT MAX(number) FROM JOKE WHERE tag = ?", (tag,))
            for row in rows:
                if row[0] == None:
                    check = False
                    conn.send("empty".encode(FORMAT))
                    num = -1

            if check:
                # Selection
                rows = cur.execute("SELECT content, score, number, count FROM JOKE WHERE tag = ? ORDER BY RANDOM() limit 1", (tag,))
                for row in rows:
                    joke = row[0]
                    conn.send(joke.encode(FORMAT))
                    conn.recv(1024)
                    score = row[1]
                    conn.send(str(score).encode(FORMAT))
                    num = row[2]  # specify which joke is selected

        elif command == "SCORE":
            print(str(addr) + " : SCORE")
            conn.send("OK".encode(FORMAT))  # response to the client

            score = float(conn.recv(1024).decode(FORMAT))
            if num > -1:
                rows = cur.execute("SELECT number, score, count FROM JOKE WHERE number = ?", (num,))
                for row in rows:
                    cnt = int(row[2]) + 1
                    new_score = round(float((row[1] * (cnt - 1) + score) / cnt), 1)

                    # Update the score in the database
                    cur.execute("UPDATE JOKE SET score = ?, count = ? WHERE number = ?", (new_score, cnt, num))
                    con.commit()

        elif command == "QUIT":
                connect = False

        elif command == "INSERT":
            print(str(addr) + " : INSERT")
            conn.send("OK".encode(FORMAT))  # response to the client

            inputJoke = conn.recv(2048).decode(FORMAT) # get the joke from the client
            conn.send("ACK".encode(FORMAT))  # response to the client

            tag = conn.recv(1024).decode(FORMAT) # get the tag from the client
            
            #Insert the joke into the database
            rows = cur.execute("SELECT MAX(number) FROM JOKE ")
            for row in rows:
                if row[0] == None:
                    number = 0
                else:
                    number = row[0]

            cur.execute("INSERT INTO JOKE VALUES (?, ?, ?, ?, ?)", (number + 1, inputJoke, tag, 0.0, 0))
            con.commit()
            
        else:
            print("Invalid command!")

    con.close()
    print(str(addr) + " : QUIT")
    conn.close()
        


def main():
    # create a server socket and bind it to the ADDR
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid address has already been used
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
