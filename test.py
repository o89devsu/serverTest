import socket
import threading
import os

def startServer():
    host = "0.0.0.0"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print("Server lauscht auf", port)
    conn, addr = s.accept()
    with conn:
        print("Verbunden mit", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Empfangene Daten", data.decode())
            if data.decode() == "lock_pc":
                os.system("rundll32.exe user32.dll,LockWorkStation")

def startClient():
    host = "localhost"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    user = input("Nachricht: ")
    user = user.encode("utf-8")
    s.sendall(user)

t1 = threading.Thread(target=startServer)
t2 = threading.Thread(target=startClient)

t1.start()
t2.start()