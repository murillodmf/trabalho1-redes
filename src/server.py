import socket


HOST = "0.0.0.0"
PORT = "772023"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor está aguardando conexões na porta {PORT}")

conn, addr = server.accept()
print(f"Conectado a {addr}")

while True:

    mensagem = conn.recv(1024).decode()

    if not mensagem:
        break

    print(f"Cliente: {mensagem}")

    resposta = input("Servidor: ")
    conn.send(resposta.encode())

    conn.close()
    server.close()