#!/usr/bin/python3


"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

import socket, json, sys

# Server
def run_server():
    host = input("Enter IP address to listen on (default 0.0.0.0): ").strip() or "0.0.0.0"
    try:
        port = int(input("Enter port number to listen on (default 5001): ").strip() or 5001)
    except ValueError:
        print("Invalid port number. Using default 5001.")
        port = 5001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print(f"\nServer started on {host}:{port}")
    print("Waiting for a client connection...\n")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}\n")

    buffer = ""
    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                print("Client disconnected.")
                break

            buffer += data
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                try:
                    person = json.loads(line)
                    print("Received JSON data:")
                    print(json.dumps(person, indent=4))
                    conn.sendall(b"Server: Data received successfully.\n")
                except json.JSONDecodeError:
                    print("Received invalid JSON data.")
                    conn.sendall(b"Server: Invalid JSON received.\n")

    except KeyboardInterrupt:
        print("\nServer terminated by user.")
    finally:
        conn.close()
        server_socket.close()
        print("Server closed.")


# Client
def run_client():
    host = input("Enter proxy IP address (default 0.0.0.0): ").strip() or "0.0.0.0"
    try:
        port = int(input("Enter proxy port number (default 5000): ").strip() or 5000)
    except ValueError:
        print("Invalid port number. Using default 5000.")
        port = 5000

    team = {}

    try:
        with socket.create_connection((host, port)) as sock:
            print(f"\nConnected to server at {host}:{port}\n")

            while True:
                player_fname = input("Please enter the players first name: ").strip()
                player_lname = input("Please enter the players last name: ").strip()

                try:
                    age = int(input("Please enter the players age in years: "))
                except ValueError:
                    print("Please enter a valid integer for the players age in years.\n")
                    continue

                goal = input("Has the player scored a goal? (y/n): ").strip().lower()
                goal = goal in ["Y", "y", "yes", "Yes"]

                try:
                    total_goals = int(input("Please enter the total goals the player has scored: "))
                except ValueError:
                    print("Please enter a valid integer for the total goals a player has scored.\n")
                    continue
                
                # Build one record per transmission
                team = {
                    "The players first name is" : player_fname,
                    "The players last name is" : player_lname,
                    "The players age is" : age,
                    "Has the player scored a goal" : goal,
                    "Total goals player has scored" : total_goals,
                }

                # Convert to JSON and send (newline-delimited)
                data = json.dumps(team) + "\n"
                sock.sendall(data.encode("utf-8"))
                print("Sent JSON data to server.")

                # Receive acknowledgment
                response = sock.recv(1024).decode("utf-8").strip()
                print(response + "\n")

                # Ask user if they want to continue
                cont = input("Send another entry? (y/n): ").strip().lower()
                if cont not in ["Y", "y", "yes", "Yes"]:
                    print("Closing connection.")
                    break

    except ConnectionRefusedError:
        print(f"Could not connect to proxy at {host}:{port}. Is it running?")
    except KeyboardInterrupt:
        print("\nClient terminated by user.")


# Main Entry
if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["server", "client"]:
        print("Argument needed! - python3 clientServer.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "server":
        run_server()
    else:
        run_client()
