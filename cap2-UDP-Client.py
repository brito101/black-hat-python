import socket
from urllib import response

target_host = "127.0.0.1"
target_port = 80

# create object socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
message = "AAABBBCCC"
client.sendto(message.encode('utf-8'), (target_host, target_port))

# receive data
data, addr = client.recvfrom(4096)

print(data)
