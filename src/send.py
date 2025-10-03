#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

# Importing the libaries required for this program
import socket, json

# Declare a Python dictionary data type named "person"
# to store key value pairs
person = {}

# Define the main function
def Main():
    # Initialise a variable named "thing" with Boolean value True
    thing = True
  
    # Initialise a variable named "host" with value 127.0.0.1 (localhost)
    # This is the servers IPv4 address
    host = '127.0.0.1'
  
    # Initialise a variable named "port" with value 5000
    # This is the servers port
    port = 5000
    
    # Create a socket with the socket function
    s = socket.socket()
  
    # The connect function can take arguments, the variables "host" 
    # and "port" have been passed to the connect function
    s.connect((host, port))
  
    # Print to standard output (stdout) - the CLI
    print ("You are connected to the server.")
    
    # Create an infinite while loop
    while True:
        while things:
        
            # Initialise a variable named "fname" with the Python input 
            # function, the Python input function takes input from the
            # standard input (stdin) - the CLI
            fname = input ("Please enter your first name  ")
        
            # Initialise a variable named "sname" with the Python input 
            # function
            sname = input ("Please enter your surname  ")
        
            # Initialise a variable named "age" with the Python input 
            # function and specifiy the input must be an int (integer)
            # NOT A STRING!
            age = int(input("How old are you?"))
        
            # Initialise a variable named "martial" with the Python input 
            # function
            martial = input("Married? - y/n ")
        
            # A conditional if statment to assign a Boolean value of True
            # or False to the variable "martial" dependant on the input
            if martial in ["Y","y"]
                martial = True
            else:
                martial = False
        
            # Add the variables "fname", "sname", age
            # and "marital" to the "person" dictonary
            person[fname + " " +sname] = {
                'First name' :fname,
                'Last name' :sname,
                'age' :age,
                'Marital Status' :marital
                }
            
            # Initialise a variable named "go" with the Python input 
            # function     
            go = input
      
            # A conditional if statment to assign a Boolean value of False
            # to the variable "go" dependant on if the input is x or X
            if go in ["x","X"]:
                thing = False
        
        # Print to standard output (stdout) - the CLI        
        print ("Sending your data")
        
        # Break out of the loop
        break
    input("")
    
    

# Run the Main function    
if __name__ == '__main__':
    Main()
                
