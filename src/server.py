#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

import socket, select

# Variables
CONNECTION_LIST = []
CLIENTS = {}
RECV_BUFFER = 4096
PORT = 5001
ID = 0


def broadcast_data(sender_sock, message):
    # Send message to all
    for sock in CONNECTION_LIST:
        if sock not in (server_socket, sender_sock):
            try:
                sock.send(message.encode('utf-8'))
            except Exception:
                sock.close()
                CONNECTION_LIST.remove(sock)


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
    server_socket.setblocking(False)

    CONNECTION_LIST.append(server_socket)
    print(f"Chat server started on port {PORT}")

    ID = 0

    while True:
        read_sockets, _, _ = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            # New connection
            if sock == server_socket:
                client_sock, addr = server_socket.accept()
                CONNECTION_LIST.append(client_sock)
                CLIENTS[client_sock] = addr

                ID += 1
                print(f"Client {addr} connected (ID: {ID})")

                broadcast_data(client_sock, f"[Server] Client {addr} has joined the chat.")
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        message = data.decode('utf-8')
                        print(f"Received from {CLIENTS[sock]}: {message}")
                        broadcast_data(sock, f"<{CLIENTS[sock]}> {message}")
                    else:
                        raise ConnectionResetError
                except (ConnectionResetError, ConnectionAbortedError):
                    addr = CLIENTS.get(sock, ("Unknown", ""))
                    print(f"Client {addr} disconnected.")
                    broadcast_data(sock, f"[Server] Client {addr} has left the chat.")
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    CLIENTS.pop(sock, None)
                except Exception as e:
                    print(f"Error: {e}")
                    continue

    server_socket.close()
