import socket
import threading
import sqlite3

clients = {}

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        # Receive data from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"[{client_address}] {data}")

        # Check if the received data is a login attempt
        if data.startswith("login"):
            # Extract username and password from the received data
            _, username, password = data.split()

            # Check if the username and password are valid
            if authenticate_user(username, password):
                clients[username] = client_socket  # Store client socket in dictionary
                client_socket.sendall("Login successful!".encode('utf-8'))
            else:
                client_socket.sendall("Invalid username or password.".encode('utf-8'))
        elif data.startswith("create_user"):
            # Extract username and password from the received data
            _, username, password = data.split()

            # Attempt to create a new user
            if create_user(username, password):
                client_socket.sendall("User created successfully!".encode('utf-8'))
            else:
                client_socket.sendall("Failed to create user. Please try again.".encode('utf-8'))
        else:
            # Broadcast the received message to all other connected clients
            broadcast_message(username, data)

    print(f"[DISCONNECTED] {client_address} disconnected.")
    client_socket.close()

# Function to broadcast a message to all connected clients
def broadcast_message(sender_username, message):
    for username, client_socket in clients.items():
        if username != sender_username:
            try:
                client_socket.sendall(f"[{sender_username}]: {message}".encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message to {username}: {e}")

# Function to handle establishing a connection between two clients
def establish_connection(sender_username, recipient_username):
    sender_socket = clients.get(sender_username)
    recipient_socket = clients.get(recipient_username)

    if sender_socket and recipient_socket:
        sender_socket.sendall(f"Connecting to {recipient_username}...".encode('utf-8'))
        recipient_socket.sendall(f"Connecting to {sender_username}...".encode('utf-8'))
        # Here you can implement the logic for establishing a direct connection between clients
        # For example, you can prompt the clients to agree to the connection and exchange necessary information
    else:
        sender_socket.sendall(f"User '{recipient_username}' is not connected.".encode('utf-8'))

# Function to handle client connections
# def handle_client(client_socket, client_address):
#     print(f"[NEW CONNECTION] {client_address} connected.")

#     while True:
#         # Receive data from client
#         data = client_socket.recv(1024).decode('utf-8')
#         if not data:
#             break
#         print(f"[{client_address}] {data}")

#         # Check if the received data is a login attempt
#         if data.startswith("login"):
#             # Extract username and password from the received data
#             _, username, password = data.split()

#             # Check if the username and password are valid
#             if authenticate_user(username, password):
#                 clients[username] = client_socket  # Store client socket in dictionary
#                 client_socket.sendall("Login successful!".encode('utf-8'))
#             else:
#                 client_socket.sendall("Invalid username or password.".encode('utf-8'))
#         elif data.startswith("create_user"):
#             # Extract username and password from the received data
#             _, username, password = data.split()

#             # Attempt to create a new user
#             if create_user(username, password):
#                 client_socket.sendall("User created successfully!".encode('utf-8'))
#             else:
#                 client_socket.sendall("Failed to create user. Please try again.".encode('utf-8'))
#         else:
#             # Broadcast the received message to all other connected clients
#             broadcast_message(username, data)

#     print(f"[DISCONNECTED] {client_address} disconnected.")
#     client_socket.close()

# # Function to broadcast a message to all connected clients
# def broadcast_message(sender_username, message):
#     for username, client_socket in clients.items():
#         if username != sender_username:
#             try:
#                 client_socket.sendall(f"[{sender_username}]: {message}".encode('utf-8'))
#             except Exception as e:
#                 print(f"Error broadcasting message to {username}: {e}")

def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        # Check if the user already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("User already exists.")
            return False

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User created successfully.")
        return True
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    finally:
        conn.close()

# Function to authenticate user from the database
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Query the database for the given username and password
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    # Return True if user found, False otherwise
    return user is not None

def start_server():
    # Server configuration
    server_host = "0.0.0.0"
    server_port = 9999

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"[SERVER STARTED] Listening on {server_host}:{server_port}")

    try:
        while True:
            # Accept incoming connections
            client_socket, client_address = server_socket.accept()
            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except KeyboardInterrupt:
        print("[SERVER STOPPED] Server stopped.")
        server_socket.close()

if __name__ == "__main__":
    start_server()

