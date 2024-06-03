import socket 
ip="192.168.29.68"
port=8081
format="utf-8"
addr=(ip,port)
size=1024
try:
    
        print("Waiting for connection")

        r=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        r.bind(addr)
        r.listen()
        print("Server is Listening")
        while True:
            conn,addr=r.accept()
            print(f"CONNECTED TO {addr} ")
            filename=conn.recv(size).decode(format)
            print("Filename Received")
            file=open(filename,'w')
            conn.send("Filename is Received".encode(format))
            data=conn.recv(size).decode(format)
            print(f"Received successfully data")
            file.write(data)
            conn.send("File data receive".encode(format))
            file.close()
            conn.close()
            
except:
      print("Connection Failed")