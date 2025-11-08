#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

import socket, select
ID=1

#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):

    #Do not send the message to master socket and the client who has sent us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try :
                socket.send(message.encode('utf-8'))
            except :
		#broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)
		
if __name__ == "__main__":

    #List to keep track of socket description
    CONNECTION_LIST = []
    RECV_BUFFER = 4096 #Advisable to keep is as an exponant of 2
    PORT = 5000
		
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #this has no effect, why?
    server_socket.setsockopt(socket.SOL_, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.setblocking(0)
    server_socket.listen(10)
		
    #add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
		
    print ("Chat server started on port " +str(PORT))
		
    while 1:
	#get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.selcet(CONNECTION_LIST,[],[])
        for sock in read_socket:
	    #new connection
            if sock == server_sockets:
                sockfd, addr = server_socket.accept()

                CONNECTION_LIST.append(sockfd)
                print ("Client (%s, %s) is online" % addr)
                print (ID)
                turn = IS +i
	        # sockfd.send(turn.encode('utf-8'))
	        # broadcast_data(sockfd, "The other player is turn " + turn)

	        #some incomming message from client
            else:
                try:
                    data = sock.recv(RECV_BUFFER).decode('utf-8')

                    if data:
	        	#broadcast_data(sock, data)

                        except:
                            broadcast_data(sock, "client (%s, %s) is offline" % addr)
                            print ("Client (%s, %s) is offline" % addr)
                            sock.close()
                            CONNECTION_LIST.remove(sock)
                            continue

server_socket.close()
									
                
            
