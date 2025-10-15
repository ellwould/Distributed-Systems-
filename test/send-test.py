#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

import socket

def main():
    # Initialise a variable named "thing" with Boolean value True
    thing = True
  
    # Initialise a variable named "host" with value 127.0.0.1 (localhost)
    # This is the servers IPv4 address
    host = '127.0.0.1'
  
    # Initialise a variable named "port" with value 5000
    # This is the servers port
    port = 5000

    # Join host and port variable
    addressPort = (host, port)
    
    # Create a socket with the socket function
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    # The connect function can take arguments, the variables "host" 
    # and "port" have been passed to the connect function
    sock.connect(addressPort)
  
    # Print to standard output (stdout) - the CLI
    print ("You are connected to the server.")
    
    # Create an infinite while loop
    while True:
        while thing:
        
            # Initialise a variable named "test" with the Python input 
            # function, the Python input function takes input from the
            # standard input (stdin) - the CLI
            test = input ("Please enter random string for test:  ")
            sock.send(test.encode("ascii"))
        break
    
    

# Run the main function    
if __name__ == '__main__':
    main()
