import socket
import threading

def handle_client(client_socket, addr):
    print(f"Accepted connection from {addr}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received message from {addr}: {message}")

        # Broadcast the message to all connected clients
        for client in clients:
            if client != client_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    # Remove the client if unable to send message
                    clients.remove(client)

    client_socket.close()
    print(f"Connection With {addr} Closed")

clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.20', 8080))
server.listen(5)

print("Server Connected To Port 8080")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
