import socket

# Creatig a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to a specific address and port
sock.bind(("localhost", 1234))

# Listening for incoming connections
sock.listen()

# Accepting a connection from the producer
conn, addr = sock.accept()

# Initializing the sum
total = 0

while True:
    # Receiving data from the client
    data = conn.recv(1024).decode()

    # Checking if the client has sent the end of the sequence message
    if data == "FINISH":
        break

    # Adding the received number to the sum
    total += int(data)

# Printing the final sum
print("The Sum is:", total)

# Closing the socket
sock.close()
