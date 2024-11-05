import socket
import threading

clients = []  # To store connected TCP clients

# TCP handler to relay messages between clients
def handle_tcp_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"[TCP] Received from {address}: {message.decode('utf-8')}")
                broadcast_tcp(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Broadcast a TCP message to all connected clients except the sender
def broadcast_tcp(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# UDP handler to relay messages between clients
def handle_udp(server_socket):
    while True:
        try:
            message, client_address = server_socket.recvfrom(1024)
            print(f"[UDP] Received from {client_address}: {message.decode('utf-8')}")
            broadcast_udp(server_socket, message, client_address)
        except ConnectionResetError:
            print(f"[UDP] Connection reset by {client_address}, skipping message.")
        except Exception as e:
            print(f"[UDP] Error: {e}")
            break

# Broadcast a UDP message to all clients
def broadcast_udp(server_socket, message, sender_address):
    for client in clients:
        if client.getpeername() != sender_address:
            try:
                server_socket.sendto(message, client.getpeername())
            except Exception as e:
                print(f"[UDP] Failed to send message: {e}")

def start_server():
    # Start TCP server
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('127.0.0.1', 5000))
    tcp_server.listen(5)
    print("[TCP Server] Listening on 127.0.0.1:5000")

    # Start UDP server
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(('127.0.0.1', 5001))
    print("[UDP Server] Listening on 127.0.0.1:5001")

    # Handle TCP clients
    threading.Thread(target=handle_udp, args=(udp_server,)).start()

    while True:
        client_socket, client_address = tcp_server.accept()
        print(f"[TCP] Accepted connection from {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_tcp_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_server()


