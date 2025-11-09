#!/usr/bin/python3

"""
Added a shebang on line one so the Python3 interpreter can
execute the Python file on a GNU/Linux OS

To find the absolute path for the Python3 interpreter on a 
GNU/Linux distrubution run the follwing BASH command:

whereis python3
"""

import socket, json

def main():
    host = '127.0.0.1'
    port = 5001

    person = {}

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            print("Connected to server at {}:{}".format(host, port))

            while True:
                fname = input("Please enter your first name: ").strip()
                sname = input("Please enter your surname: ").strip()

                try:
                    age = int(input("How old are you? "))
                except ValueError:
                    print("Please enter a valid integer for age.")
                    continue

                marital = input("Married? (y/n): ").strip().lower()
                marital = marital in ["y", "yes"]

                # Build a dictionary entry
                person[f"{fname} {sname}"] = {
                    "First name": fname,
                    "Last name": sname,
                    "Age": age,
                    "Marital Status": marital
                }

                # Convert to JSON and send
                data = json.dumps(person)
                sock.sendall(data.encode("utf-8"))
                print("Sent JSON data to server.")

                # Ask user if they want to send more
                cont = input("Send another entry? (y/n): ").strip().lower()
                if cont not in ["y", "yes"]:
                    print("Closing connection.")
                    break

    except ConnectionRefusedError:
        print("Could not connect to server. Is it running?")
    except KeyboardInterrupt:
        print("Client terminated by user.")


if __name__ == "__main__":
    main()
