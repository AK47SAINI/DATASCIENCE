import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address="192.168.180.35"

    port=8080          
    target=(ip_address,port)
    s.bind(target)

    message=s.recvfrom(120)
    data=message[0]
        
    print(data)
        # print(data.encode('ascii'))
except Exception as e:
    print("i can't get your message")
else:
    print("I got your message")