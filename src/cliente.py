import socket

HOST = input("Digite o IP do servidor: ")
PORT = int(input("Digite a porta: "))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Conectado ao servidor. Digite 'sair' para encerrar.")

while True:

    mensagem = input("Cliente: ")
    client.send(mensagem.encode())

    if mensagem.lower() == "sair":
        break

    resposta = client.recv(1024).decode()
    print(f"Servidor: {resposta}")

client.close()
