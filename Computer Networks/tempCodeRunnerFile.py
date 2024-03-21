from socket import *


def send_temperature_to_server():
    serverName = '172.30.78.75'  # or 'hostname' 'IP address'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Prompt user for input
    celsius = float(input('Enter the temperature in Celsius: '))

    # Send temperature to server
    clientSocket.sendto(str(celsius).encode(), (serverName, serverPort))

    # Receive modified message from server
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Received message from %s port %s" %
          (serverAddress[0], serverAddress[1]))

    # Print the modified message received from server
    print("Converted temperature:", modifiedMessage.decode())

    # Close the socket
    clientSocket.close()


# Call the function to send temperature to the server
send_temperature_to_server()
