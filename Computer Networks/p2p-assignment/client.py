import socket
import threading

def receive_messages(client_socket):
    while True:
        # Receive messages from server
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("[SERVER]", data)

def start_client():
    # Server configuration
    server_host = "127.0.0.1"
    server_port = 9999

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client_socket.connect((server_host, server_port))
        print("[CONNECTED] Connected to server.")

        while True:
            # Prompt user for action: login or create_user
            action = input("Enter 'login' to log in or 'create_user' to create a new user: ")

            if action == 'login':
                # Prompt user for login credentials
                username = input("Enter username: ")
                password = input("Enter password: ")

                # Send login attempt to server
                login_attempt = f"login {username} {password}"
                client_socket.sendall(login_attempt.encode('utf-8'))

                # Receive response from server
                response = client_socket.recv(1024).decode('utf-8')
                print("[SERVER]", response)
                if response == "Login successful!":
                    break
            elif action == 'create_user':
                # Prompt user to create a new user
                username = input("Enter new username: ")
                password = input("Enter new password: ")

                # Send create_user request to server
                create_user_request = f"create_user {username} {password}"
                client_socket.sendall(create_user_request.encode('utf-8'))

                # Receive response from server
                response = client_socket.recv(1024).decode('utf-8')
                print("[SERVER]", response)
            else:
                print("Invalid action. Please enter 'login' or 'create_user'.")

        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        # Main loop for sending messages
        while True:
            # Send messages to server
            message = input()
            client_socket.sendall(message.encode('utf-8'))

    except ConnectionRefusedError:
        print("[CONNECTION ERROR] Connection refused. Make sure the server is running.")
    except KeyboardInterrupt:
        print("[DISCONNECTING] Disconnecting from server.")
        client_socket.close()

if __name__ == "__main__":
    start_client()
