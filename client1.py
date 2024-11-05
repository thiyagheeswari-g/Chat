import socket
import threading

# Function to receive messages from the server
def receive_messages(tcp_socket):
    while True:
        try:
            message = tcp_socket.recv(1024).decode('utf-8')
            print(f"Message from other client: {message}")
        except:
            print("Connection closed by server.")
            break

# TCP connection setup
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('127.0.0.1', 5000))

# UDP connection setup
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start a thread to listen for incoming TCP messages
threading.Thread(target=receive_messages, args=(tcp_socket,)).start()

while True:
    message = input("Enter message to send: ")
    
    # Send via TCP
    tcp_socket.send(message.encode('utf-8'))
    
    # Optionally, you can send via UDP (if needed for faster messaging)
    udp_socket.sendto(message.encode('utf-8'), ('127.0.0.1', 5001))
