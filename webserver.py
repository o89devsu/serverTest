import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname())

HOST = '0.0.0.0'
PORT = 12345
TARGET_HOST = local_ip
TARGET_PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    conn, addr = server_socket.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as target_socket:
                target_socket.connect((TARGET_HOST, TARGET_PORT))
                target_socket.sendall(data)
