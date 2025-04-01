import socket

# Configuração do servidor
HOST = "0.0.0.0"  # Aceita conexões de qualquer IP
PORT = 7720        # Porta usada para comunicação

# Criando o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reuso da porta

server.bind((HOST, PORT))  # Associa o socket ao endereço e porta
server.listen(1)  # Aguarda conexões

print(f"Servidor aguardando conexões na porta {PORT}...")

conn, addr = server.accept()  # Aceita a conexão
print(f"Conectado a {addr}")

# Troca de mensagens
while True:
    # Recebe mensagem do cliente
    mensagem_cliente = conn.recv(1024).decode('utf-8')
    if mensagem_cliente.lower() == 'sair':
        print("Cliente desconectado.")
        break
    print(f"Cliente: {mensagem_cliente}")

    # Envia mensagem para o cliente
    mensagem_servidor = input("Digite sua mensagem: ")
    conn.sendall(mensagem_servidor.encode('utf-8'))
    if mensagem_servidor.lower() == 'sair':
        print("Desconectando...")
        break

# Fecha a conexão
conn.close()
