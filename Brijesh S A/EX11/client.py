import socket
host='127.0.0.1'
port=5001
obj=socket.socket()
obj.connect((host,port))
message=input("Type Message :")

while message !='bye':
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    print('Recieved from server : '+data)
    message=input("Type Message :")
obj.send(message.encode())
obj.close()