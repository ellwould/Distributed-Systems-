#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

import socket, sys, select

BUFFER_SIZE = 4096

if __name__ == "__main__":
    # Configure listening
    listen_host = input("Enter IP address to listen on (default 0.0.0.0): ").strip() or "0.0.0.0"
    try:
        listen_port = int(input("Enter port to listen on (default 5000): ").strip() or 5000)
    except ValueError:
        listen_port = 5001

    # Configure sending
    send_host = input("Enter target IP address to forward data to (default 0.0.0.0): ").strip() or "0.0.0.0"
    try:
        send_port = int(input("Enter target port (default 5001): ").strip() or 5001)
    except ValueError:
        send_port = 5001

    # Create listening socket
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind((listen_host, listen_port))
    listen_sock.listen(5)
    print(f"Listening on {listen_host}:{listen_port}")
    print(f"Sending to {send_host}:{send_port}")

    try:
        while True:
            # Incoming connection
            client_sock, client_addr = listen_sock.accept()
            print(f"Connection from {client_addr}")

            # Sending connection
            send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                send_sock.connect((send_host, send_port))
            except Exception as e:
                print(f"Could not connect to target: {e}")
                client_sock.close()
                continue

            # Relay data between client and target
            sockets = [client_sock, send_sock]

            try:
                while True:
                    read_socks, _, _ = select.select(sockets, [], [])
                    for s in read_socks:
                        data = s.recv(BUFFER_SIZE)
                        if not data:
                            raise ConnectionResetError

                        # Send data
                        if s is client_sock:
                            send_sock.sendall(data)
                            print(f"Sent {len(data)} bytes from client to server")
                        else:
                            client_sock.sendall(data)
                            print(f"Sent {len(data)} bytes from server to client")

            except (ConnectionResetError, ConnectionAbortedError):
                print("Connection closed.")
                client_sock.close()
                sent_sock.close()

    except KeyboardInterrupt:
        print("\nShutting down proxy program.")
        listen_sock.close()
