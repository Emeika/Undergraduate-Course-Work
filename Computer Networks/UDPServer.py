from socket import *


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message received from %s port %s" %
          (clientAddress[0], clientAddress[1]))

    # Assuming the message contains Celsius temperature as a float
    celsius = float(message.decode())
    fahrenheit = celsius_to_fahrenheit(celsius)

    # Modify the message to include Fahrenheit temperature
    modifiedMessage = f"{celsius} Celsius is {fahrenheit} Fahrenheit"

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
