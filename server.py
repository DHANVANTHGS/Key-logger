import socket

#to listen all ip's which would get connected
Host='0.0.0.0'
port=3001

#establish connection on ipv4 and using TCP protocol
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((Host,port))
server.listen(5)   #queues 5 users

print(f"Server listening on {Host}:{port}...")

while True:
    #to accept the connection 
    conn,addr=server.accept()

    print(f"Connected by {addr}")

    fname=conn.recv(1024).decode().strip()

    print(f"Receiving file: {fname}")
    #to get data from user and store in our system
    with open (fname,"wb") as f:
        try :
            while True:
                data=conn.recv(1024)
                if not data:
                    break
                f.write(data)
                print("received data:",data.decode())
        except ConnectionResetError :
            print("connection closed:")
        finally :
            conn.close()

server.close()

        
