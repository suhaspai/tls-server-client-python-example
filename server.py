"""
Server Side:
A socket is created and bound to localhost on port 8443.
The socket is wrapped with SSL using a context that loads the
server's certificate and private key. The server listens for incoming
connections, accepts them, and communicates securely.
"""

import socket
import ssl

PORT = 8443

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))
server_socket.listen(5)

# Wrap the socket with SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='./server.crt', keyfile='./server.key')

with context.wrap_socket(server_socket, server_side=True) as tls_server_socket:
    print("Server is listening on port %d ...", PORT)
    while True:
        client_socket, addr = tls_server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        client_socket.sendall(b"Hello, TLS Client!")
        client_socket.close()
