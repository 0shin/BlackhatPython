# -*- coding: utf-8 -*-

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#  Thread to handle connection from client
def handle_client(client_socket):
    
    # Display data sent from client
    request = client_socket.recv(1024)
    
    print "[*] Recived: %s" % request
    
    # reply packet
    client_socket.send("ACK!")

while True:
    
    client, addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
    
    #Thread to hanndle recived data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    