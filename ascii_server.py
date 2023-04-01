import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 1826

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

# Wait for incoming connections
print('Server listening on {}:{}'.format(HOST, PORT))
conn, addr = server_socket.accept()
print('Connected by', addr)

# Receive data from client and send response back
while True:
    data = conn.recv(1024)
    if not data:
        break
    # Convert data to ASCII code
    ascii_codes = [str(ord(ch)) for ch in data.decode()]
    response = ', '.join(ascii_codes)

    conn.send(response.encode())

# Close the connection
conn.close()
