# client.py

import socket
import threading
import os


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("[SERVER] Connection closed by server.")
                break
            print(data.decode('utf-8'))
        except ConnectionAbortedError:
            print("[CLIENT] Connection aborted by client.")
            break
        except ConnectionResetError:
            print("[CLIENT] Connection reset by client.")
            break


def send_file(client_socket, file_path):
    file_name = os.path.basename(file_path)
    client_socket.sendall(f"file {file_name}".encode('utf-8'))

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            client_socket.sendall(chunk)


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

        # receive_thread = threading.Thread(
        #     target=receive_messages, args=(client_socket,))
        # receive_tshread.start()

        # while True:
        #     # Check if there is data to be read from the server
        #     ready_to_read, _, _ = select.select([client_socket], [], [], 0.1)

        #     # If there is data to be read, receive and display it
        #     for sock in ready_to_read:
        #         data = sock.recv(1024).decode('utf-8')
        #         if not data:
        #             print("[SERVER] Connection closed by server.")
        #             client_socket.close()
        #             return
        #         print(data)

        while True:
            action = input(
                "\nEnter\n'connect' to establish a direct connection with another user\n'view' to request currently connected clients\n'quit' to exit: ")

            if action == 'connect':
                recipient_username = input(
                    "Enter the username of the user you want to connect with: ")
                connect_request = f"connect {username} {recipient_username}"
                client_socket.sendall(connect_request.encode('utf-8'))

                receive_thread = threading.Thread(
                    target=receive_messages, args=(client_socket,))
                receive_thread.start()

                connected = True
                while connected:
                    communication_mode = input(
                        "\nEnter 'msg' to send a message or 'file' to send a file: ")

                    if communication_mode == 'msg':
                        while True:
                            message = input()
                            if message == 'quit':
                                connected = False
                                client_socket.sendall("quit".encode('utf-8'))
                                client_socket.close()
                                break
                            client_socket.sendall(message.encode('utf-8'))

                    elif communication_mode == 'file':
                        while True:
                            file_path = input(
                                "Enter the path of the file: ")
                            if os.path.exists(file_path):
                                send_file(client_socket, file_path)
                                print("File sent successfully.")
                                break
                            else:
                                print(
                                    "File not found. Please enter a valid file path.")
                    else:
                        print(
                            "Invalid communication mode. Please enter 'msg' or 'file'.")

            elif action == 'view':
                client_socket.sendall("request_clients".encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                print("Currently connected clients:", response)
            elif action == 'quit':
                client_socket.sendall("quit".encode('utf-8'))
                client_socket.close()
                return
            else:
                print("Invalid action.")

    except ConnectionRefusedError:
        print("[CONNECTION ERROR] Connection refused. Make sure the server is running.")
    except KeyboardInterrupt:
        print("[DISCONNECTING] Disconnecting from server.")
        client_socket.close()


if __name__ == "__main__":
    start_client()
