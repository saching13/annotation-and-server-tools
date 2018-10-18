import socket
import thread
import os
import sys


def Sendimages( threadName, c):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    while True:
       c.send("Next image")

       f=open(file, "rb")               #read image
       l = f.read()
       c.send(l)
       f.close()
       data = c.recv(4064)
       print data
       #if(c.recv(4064))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Create a socket object

host = socket.gethostname()# Get local machine name
hostname = host + ".local"
ip = socket.gethostbyname_ex(hostname)[1] # Get local machine name
print socket.gethostbyname_ex(hostname)[2]
port = 1500                # Reserve a port for your service.
s.bind((host, port))
print 'Got connection from', ip
s.listen(1)  # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   thread.start_new_thread(Sendimages, ("Thread-1", c))
   c.send('Thank you for connecting')
   c.close()
   # Close the connection