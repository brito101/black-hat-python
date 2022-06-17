import socket

target_host = "0.0.0.0"
target_port = 9999

# create object socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting client
client.connect((target_host, target_port))

# send data
message = "AAABBBCCC"
client.sendto(message.encode('utf-8'), (target_host, target_port))

# receive data
response = client.recv(4096)

print(response.decode())
