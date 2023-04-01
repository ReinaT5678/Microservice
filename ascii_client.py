from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 1826

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((HOST, PORT))

@app.route('/')
def index():
    return render_template('ascii.html')

@app.route('/process', methods=['POST'])
def convert():
    user_input = request.form['message']
    # Send the input to the server
    client_socket.send(user_input.encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode()

    return render_template('ascii.html', output=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5045)

# Close the connection
client_socket.close()
