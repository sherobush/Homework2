import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

try:
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(message, end="")

        if "Enter your account name and password" in message or "Enter amount" in message or "Choose an option" in message:
            user_input = input()
            client_socket.send(user_input.encode())

finally:
    client_socket.close()