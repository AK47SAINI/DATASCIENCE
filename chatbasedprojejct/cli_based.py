#port limit from 0 to 6553
# 192.168.180.35 ip address of our laptop
# port = 8888
import socket 
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    ip_address = "192.168.180.72"
    port=8080
    target=(ip_address,port)
    message=input("what message do you want to send")
    encripted_message=message.encode('ascii')
    s.sendto(encripted_message,target)


except Exception as e:
    print("message sending failed ")
else:
    print("Message sended successfully")
finally:
    print("Thanks for Using python!!")
