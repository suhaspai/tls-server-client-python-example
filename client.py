"""
Client Side:
A socket is created and wrapped with SSL using a context that verifies
the server's certificate. The client connects to the server, sends a message,
and receives a response securely.
Make sure you have the necessary certificate (server.crt) and key (server.key)
files for the server, and the certificate (server.crt) for the client to verify
the server's identity.
"""


import socket
import ssl

PORT = 8443

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
context = ssl.create_default_context()

context.load_verify_locations('./server.crt')

with context.wrap_socket(client_socket, server_hostname='localhost') as tls_client_socket:
    tls_client_socket.connect(('localhost', PORT))
    tls_client_socket.sendall(b"Hello, TLS Server!")
    data = tls_client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
