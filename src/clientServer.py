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
    host = input("Enter IP address to listen on (default 127.0.0.1): ").strip() or "127.0.0.1"
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
    host = input("Enter proxy IP address (default 127.0.0.1): ").strip() or "127.0.0.1"
    try:
        port = int(input("Enter proxy port number (default 5000): ").strip() or 5000)
    except ValueError:
        print("Invalid port number. Using default 5000.")
        port = 5000

    club = {}

    try:
        with socket.create_connection((host, port)) as sock:
            print(f"\nConnected to server at {host}:{port}\n")

            while True:
                club_name = input("Please enter the clubs/teams name: ").strip()
                club_country = input("Please enter the country the club/team is located in: ").strip()
                club_city = input("Please enter the city the club/team is located in: ").strip()

                try:
                    year = int(input("The current year is ? "))
                except ValueError:
                    print("Please enter a valid integer for the current year.\n")
                    continue

                try:
                    age = int(input("How many years old is the club? "))
                except ValueError:
                    print("Please enter a valid integer for how many years old the club is.\n")
                    continue

                try:
                    total_matches = int(input("How many matches in total will the team play this year? "))
                except ValueError:
                    print("Please enter a valid integer for the total ammount of matches the club will play.\n")
                    continue

                try:
                    won = int(input("How many matches won this year? "))
                except ValueError:
                    print("Please enter a valid integer for matches won.\n")
                    continue

                try:
                    lost = int(input("How many matches lost this year? "))
                except ValueError:
                    print("Please enter a valid integer for matches lost.\n")
                    continue

                try:
                    draw = int(input("How many matches drawn this year? "))
                except ValueError:
                    print("Please enter a valid integer for matches drawn.\n")
                    continue

                league = input("Is the club in the Premier League? (y/n): ").strip().lower()
                league = league in ["Y", "y", "yes", "Yes"]

                total_games_played = won + lost + draw
                
                # Build one record per transmission
                club = {
                    "Club/Team name is" : club_name,
                    "Country club/Team are from" : club_country,
                    "City club/team are from" : club_city,
                    "The current year is" : year,
                    "The football clubs age in years is" : age,
                    "Matches won this year are" : won,
                    "Matches lost this year are" : lost,
                    "Matches drawn this year are" : draw,
                    "Matches played so far this year are" : total_games_played,
                    "Matches remaining for this year are" : total_matches - total_games_played,
                    "Premier League status is" : league
                }

                # Convert to JSON and send (newline-delimited)
                data = json.dumps(club) + "\n"
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
