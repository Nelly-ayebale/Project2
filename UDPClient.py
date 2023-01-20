import socket
import random

# Creating a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
sock.connect(("localhost", 1234))

while True:
    # Generating a random number
    num = random.randint(0, 100)

    # Sending the number to the server
    sock.sendall(str(num).encode())

    # Checking if the server wants to stop
    if num == 0:
        break

# Sending a message to signal the end of the sequence
sock.sendall("FINISH".encode())
print("FINISH")

# Closing the socket
sock.close()
