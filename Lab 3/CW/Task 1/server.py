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

print("server is Listening .....")

conn, addr= server.accept()

disconnect="End"

connected=True

while connected:

    msg_length=conn.recv(data).decode(format)

    if msg_length:

        msg_length= int(msg_length)

        msg=conn.recv(msg_length).decode(format)

        if msg==disconnect:

            connected=False

            conn.send("Goodbye!".encode(format))

        else:
            
            print(msg)
            
            conn.send("Meesage Received!".encode(format))

conn.close()
            