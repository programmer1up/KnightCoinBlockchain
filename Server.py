import socket
import sys
import time
import datetime

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Successfully...")
except socket.error:
    print("Failed to create socket...")

def Connect():

    host = 'localhost'

    port = 8888

    try:
        remote_ip = socket.gethostbyname(host)
        #socket.gethostbyaddr("192.168.1.135")
        #
    except socket.gaierror:
        print ("Hostname could not be resolved, exiting...")
        sys.exit()

    print("IP address of "+host+" is "+remote_ip)

    s.connect((remote_ip,port))

    print ("Socket connected to "+host+" on "+remote_ip)

def sendData():
    message = "hello"
    #"GET / HTTP/1.1\r\n\r\n"
    try:
        s.sendall(message.encode())
        print("Message Sent")
    except socket.error:
        print ("Message Failed to send")

def receiveData():
    reply = s.recv(4096)
    print (reply)
Connect()
sendData()
receiveData()
