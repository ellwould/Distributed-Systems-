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

# Define the main function
def main():
    # Server host and port configuration
    host = '127.0.0.1'
    port = 5000

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}")

    # Listen for incoming connections
    server_socket.listen(2)
    print("Waiting for a connection...")

    # Accept a client connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        # Data from the client
        data = conn.recv(1024).decode("utf-8")

        if not data:
            # If no data is received, the client disconnected
            print("Client disconnected.")
            break

        print(f"Raw data received:\n{data}")

        # Parse the JSON data
        try:
            person = json.loads(data)
            print("Decoded JSON data:")
            print(json.dumps(person, indent=4))
        except json.JSONDecodeError:
            print("Received invalid JSON data.")

    # Close the connection
    conn.close()
    server_socket.close()
    print("Server closed.")


# Run the main function
if __name__ == '__main__':
    main()
