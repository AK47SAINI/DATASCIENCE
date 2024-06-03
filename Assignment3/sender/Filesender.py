import socket

# Configuration
ip = "192.168.29.68"
port = 8081
format = "utf-8"
addr = (ip, port)
size = 1024

try:
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    
    # Get filename from user
    filename = input("Enter the file name that you want to send: ")

    # Open the file
    with open(filename, 'r') as file:
        data = file.read()
        
    # Send filename to server
    s.send(filename.encode(format))
    
    # Receive confirmation from server
    msg = s.recv(size).decode(format)
    print(f"[SERVER]: {msg}")

    # Send file data to server
    s.send(data.encode(format))

    # Receive final confirmation from server
    msg = s.recv(size).decode(format)
    print(f"[SERVER]: {msg}")

    # Close the socket
    s.close()


except FileNotFoundError:
    print("File not found! Please enter a valid filename.")
except ConnectionError:
    print("Connection failed! Please check the server IP and port.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Successfully sended to the Receiver")