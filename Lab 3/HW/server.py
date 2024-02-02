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

print("Server is Listening .....")

conn, addr= server.accept()

connected = True

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

            value = int(msg)
            
            if value <= 40:

                total = value * 200

                total = "Tk " + str(total)

                conn.send(total.encode(format))

            elif value > 40:

                extra_hour = value - 40

                extra_money = extra_hour * 300

                total = 8000 + extra_money

                total = "Tk " + str(total)         

                conn.send(total.encode(format))

conn.close()
            