import socket

Host='0.0.0.0'
port=3001

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((Host,port))
server.listen(5)

print(f"Server listening on {Host}:{port}...")

while True:

    conn,addr=server.accept()

    print(f"Connected by {addr}")

    fname=conn.recv(1024).decode().strip()

    print(f"Receiving file: {fname}")

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

        
