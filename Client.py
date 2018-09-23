import sys
import socket

HOST = ""
PORT = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created...")

try:
    s.bind((HOST,PORT))
except socket.error:
    print ("Bind failed")
    sys.exit()

print("Socket bind complete...")

s.listen(10)

conn, addr = s.accept()

print("Connected with" + addr[0] + ":" +str(addr[1]))

while True:
            data = conn.recv(4096)
            print (data)
            if data:
                #print >>sys.stderr, 'sending data back to the client'
                conn.sendall(data+(",again...").encode())
            else:
                #print >>sys.stderr, 'no more data from', addr
                break

