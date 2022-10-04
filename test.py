import socket
import ssl

hostname = 'hasthelargehadroncolliderdestroyedtheworldyet.com'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        try:
            print(ssock.version())
        except Exception as err:
            print(err.__dict__)