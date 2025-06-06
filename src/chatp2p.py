import socket
import threading


# Thread para escutar mensagens recebidas
def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"\nPeer: {msg}")
            else:
                print("[DESCONEXÃO] O peer desconectou.")
                break
        except Exception as e:
            print(f"[ERRO AO RECEBER] {e}")
            break


# Thread para enviar mensagens
def send_messages(sock):
    while True:
        try:
            msg = input()
            sock.send(msg.encode())
        except Exception as e:
            print(f"[ERRO AO ENVIAR] {e}")
            break


# Thread que escuta conexões (modo servidor)
def server_thread(local_ip, local_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_ip, local_port))
    server.listen(1)
    print(f"[SERVIDOR] Escutando em {local_ip}:{local_port}...")
    conn, addr = server.accept()
    print(f"[CONECTADO COMO SERVIDOR] com {addr[0]}:{addr[1]}")

    # Cria threads de envio e recebimento
    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
    threading.Thread(target=send_messages, args=(conn,), daemon=True).start()


# Função para conectar ao peer (modo cliente)
def connect_to_peer(dest_ip, dest_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((dest_ip, dest_port))
        print(f"[CONECTADO COMO CLIENTE] a {dest_ip}:{dest_port}")

        # Cria threads de envio e recebimento
        receivethread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
        receivethread.start()

        sendthread = threading.Thread(target=send_messages, args=(client,), daemon=True)
        sendthread.start()

        receivethread.join()
        sendthread.join()

    except Exception as e:
        print(f"[FALHA NA CONEXÃO] {e}")


# Programa principal
if __name__ == "__main__":
    print("=== Chat TCP Peer to Peer ===")
    escolha = input("Digite se voce deseja se conectar ou ser conectado 'c' ou 'l' \n")
    if escolha == "l":
        local_ip = input("Digite seu IP local: ")
        local_port = int(input("Digite sua porta local: "))
        server_thread(local_ip, local_port)
    elif escolha == "c":
        dest_ip = input("Digite o IP do peer de destino: ")
        dest_port = int(input("Digite a porta do peer de destino: "))
        connect_to_peer(dest_ip, dest_port)
    else:
        print("Digite'c'ou'l'")