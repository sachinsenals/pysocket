import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(('192.168.8.106',1234))


server.listen(5)

print("Waiting For Client To Join The Chat")

client , addr = server.accept()

client.send(bytes("Welcome To The Chat","utf-8"))

print("Client Joined The Chat")



while True: 
    msg = client.recv(1024).decode('utf-8')
    
    if msg == "exit":
        client.send(bytes("exit","utf-8"))
        print("Client Left The Chat")
        break
    
    else:
        print(msg)
        msg = input("Enter Message: ")
        client.send(bytes(msg,"utf-8"))
        
server.close()
      
      
      
      