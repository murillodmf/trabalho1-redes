import socket

# Configuração do cliente
HOST = input("Digite o IP do servidor: ")  # IP do servidor
PORT = 7720  # Porta usada para comunicação

# Criando o socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client.connect((HOST, PORT))

# Troca de mensagens
while True:
    # Envia mensagem para o servidor
    mensagem_cliente = input("Digite sua mensagem: ")
    client.sendall(mensagem_cliente.encode('utf-8'))
    if mensagem_cliente.lower() == 'sair':
        print("Desconectando...")
        break

    # Recebe resposta do servidor
    mensagem_servidor = client.recv(1024).decode('utf-8')
    print(f"Servidor: {mensagem_servidor}")

# Fecha a conexão
client.close()
