import socket

format="utf8"

data=16

port=5050

hostname = socket.gethostname()

host_addr=socket.gethostbyname(hostname)

server_socket_addr=(host_addr, port)

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_socket_addr)

disconnect ="End"

def send(msg):
    
    message = msg.encode(format)

    msg_length = len(message) 

    send_length = str(msg_length).encode(format)
 
    send_length+=b' '*(data-len(send_length))
    
    client.send(send_length)

    client.send(message)

    print(client.recv(2048).decode(format))
     
send(f"Client's IP Address is {host_addr} and Client's Device name is {socket.gethostname()}")

send(disconnect)