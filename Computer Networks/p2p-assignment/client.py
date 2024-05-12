# client.py

import socket
import threading


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("[SERVER]", data)


def start_client():
    server_host = "127.0.0.1"
    server_port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_host, server_port))
        print("[CONNECTED] Connected to server.")

        logged_in = False

        while not logged_in:
            action = input(
                "Enter 'login' to log in or 'create_user' to create a new user: ")

            if action == 'login':
                validate_login = False
                while not validate_login:
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    login_attempt = f"login {username} {password}"
                    client_socket.sendall(login_attempt.encode('utf-8'))
                    response = client_socket.recv(1024).decode('utf-8')
                    print("[SERVER]", response)
                    if response == "Login successful!":
                        logged_in = True
                        validate_login = True
                    # else:
                        # print("Invalid username or password. Try again.")
            elif action == 'create_user':
                username = input("Enter new username: ")
                password = input("Enter new password: ")
                create_user_request = f"create_user {username} {password}"
                client_socket.sendall(create_user_request.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                print("[SERVER]", response)
            else:
                print("Invalid action. Please enter 'login' or 'create_user'.")

        client_socket.sendall("request_clients".encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print("Currently connected clients:", response)

        while True:
            action = input(
                "\nEnter\n'connect' to establish a direct connection with another user\n'view' to request currently connected clients\n'quit' to exit: ")

            if action == 'connect':
                recipient_username = input(
                    "Enter the username of the user you want to connect with: ")
                connect_request = f"connect {username} {recipient_username}"
                client_socket.sendall(connect_request.encode('utf-8'))
                break
            elif action == 'view':
                client_socket.sendall("request_clients".encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                print("Currently connected clients:", response)
            elif action == 'quit':
                client_socket.close()
                return
            else:
                print("Invalid action.")

        receive_thread = threading.Thread(
            target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            message = input()
            client_socket.sendall(message.encode('utf-8'))

    except ConnectionRefusedError:
        print("[CONNECTION ERROR] Connection refused. Make sure the server is running.")
    except KeyboardInterrupt:
        print("[DISCONNECTING] Disconnecting from server.")
        client_socket.close()


if __name__ == "__main__":
    start_client()
