import socket
from urllib import response

target_host = "www.rodrigobrito.dev.br"
target_port = 80

# create object socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting client
client.connect((target_host, target_port))

# send data
message = "GET / HTTP/1.1\r\nHost: rodrigobrito.dev.br\r\n\r\n"
client.sendto(message.encode('utf-8'), (target_host, target_port))

# receive data
response = client.recv(4096)

print(response.decode())
