import socket

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

#bind the address
ADDR=(SERVER, PORT) #binding IP and port
FORMAT="utf8"
DISCONNET_MSG="End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, TCP)

server.bind(ADDR)



server.listen()
print("server is Listening")

conn, addr= server.accept()

connected=True

while connected: #client is connected
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length= int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT) # how many length of messages
        if msg==DISCONNET_MSG:
            connected=False
            conn.send("Goodbye".encode(FORMAT))
            
        else:

            #write your code here

            value = int(msg)
            
            if value <= 40:

                total = value * 200

                total = "Tk " + str(total)

                conn.send(total.encode(FORMAT))

            elif value > 40:

                extra_hour = value - 40

                extra_money = extra_hour * 300

                total = 8000 + extra_money

                total = "Tk " + str(total)         

                conn.send(total.encode(FORMAT))

conn.close()
            