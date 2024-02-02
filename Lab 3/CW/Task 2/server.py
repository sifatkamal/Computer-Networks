import socket

format="utf8"

data=16

port=5050

hostname = socket.gethostname()

host_addr=socket.gethostbyname(hostname)

server_socket_addr=(host_addr, port)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_addr)

server.listen()

print("server is Listening .......")

conn, addr= server.accept()

connected=True

disconnect="End"

while connected:

    msg_length=conn.recv(data).decode(format)

    if msg_length:

        msg_length= int(msg_length)

        msg=conn.recv(msg_length).decode(format)

        if msg==disconnect:

            connected=False

            conn.send("Goodbye!".encode(format))
            
        else:

            vowels = "aeiouAEIOU"
            
            count = 0
            
            for i in msg:
                
                if i in vowels:
                    
                    count+=1
                    
            if count < 1:
                
                conn.send("Not enough vowels ".encode(format))
                
            elif count <= 2:
                
                conn.send("Enough vowels I guess ".encode(format))
                
            else:
                
                conn.send("Too many vowels ".encode(format))            

conn.close()
            