import socket

c = socket.socket()

c.connect(('192.168.197.194',5001))

email = input("Enter Your Email: ")
c.send(bytes(email, 'utf-8'))

print(c.recv(1024).decode())