import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QFileDialog, QMessageBox
import socket
import threading
import os


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P2P Chat and File Sharing")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.username_field = QLineEdit()
        self.layout.addWidget(self.username_field)

        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_field)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.create_user_button = QPushButton("Create User")
        self.create_user_button.clicked.connect(self.create_user)
        self.layout.addWidget(self.create_user_button)

        self.view_connections_button = QPushButton("View Connections")
        self.view_connections_button.clicked.connect(self.view_connections)
        self.layout.addWidget(self.view_connections_button)

        self.recipient_field = QLineEdit()
        self.layout.addWidget(self.recipient_field)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_recipient)
        self.layout.addWidget(self.connect_button)

        self.messages_display = QTextEdit()
        self.messages_display.setReadOnly(True)
        self.layout.addWidget(self.messages_display)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.file_button = QPushButton("Send File")
        self.file_button.clicked.connect(self.choose_file)
        self.layout.addWidget(self.file_button)

        self.client_socket = None
        self.username = None

        self.start_client()

    def start_client(self):
        server_host = "127.0.0.1"
        server_port = 9999

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client_socket.connect((server_host, server_port))
            self.display_message("[CONNECTED] Connected to server.")

            # message receiving thread
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
        except ConnectionRefusedError:
            self.display_message(
                "[CONNECTION ERROR] Connection refused. Make sure the server is running.")

    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if not username or not password:
            QMessageBox.warning(
                self, "Warning", "Please enter username and password.")
            return

        login_attempt = f"login {username} {password}"
        self.client_socket.sendall(login_attempt.encode('utf-8'))
        self.username = username

    def create_user(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if not username or not password:
            QMessageBox.warning(
                self, "Warning", "Please enter username and password.")
            return

        create_user_request = f"create_user {username} {password}"
        self.client_socket.sendall(create_user_request.encode('utf-8'))

    def view_connections(self):
        self.client_socket.sendall("request_clients".encode('utf-8'))

    def connect_to_recipient(self):
        recipient_username = self.recipient_field.text()

        if not recipient_username:
            QMessageBox.warning(
                self, "Warning", "Please enter recipient's username.")
            return

        connect_request = f"connect {self.username} {recipient_username}"
        self.client_socket.sendall(connect_request.encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    self.display_message(
                        "[SERVER] Connection closed by server.")
                    break
                message = data.decode('utf-8')

                if message.startswith("FILE_TRANSFER:"):
                    file_info = message.split(": ")
                    file_name = file_info[1]
                    self.display_message(f"Received file: {file_name}")
                    save_path, _ = QFileDialog.getSaveFileName(
                        self, "Save File", os.path.basename(file_name))
                    with open(save_path, 'wb') as file:
                        while True:
                            file_data = self.client_socket.recv(1024)
                            if not file_data:
                                break
                            file.write(file_data)
                    self.display_message("File saved successfully.")
                else:
                    self.display_message(message)

            except ConnectionAbortedError:
                self.display_message("[CLIENT] Connection aborted by client.")
                break
            except ConnectionResetError:
                self.display_message("[CLIENT] Connection reset by client.")
                break

    def send_message(self):
        message = self.input_field.text()
        if message:
            self.client_socket.sendall(message.encode('utf-8'))
            self.input_field.clear()
            self.display_message(f"[{self.username}]: {message}")

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose File")
        if file_path:
            self.send_file(file_path)

    def send_file(self, file_path):
        file_name = os.path.basename(file_path)
        self.client_socket.sendall(f"file {file_name}".encode('utf-8'))

        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                self.client_socket.sendall(chunk)

    def display_message(self, message):
        self.messages_display.append(message)


def main():
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
