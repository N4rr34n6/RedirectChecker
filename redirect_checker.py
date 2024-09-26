import requests
import re
import sys
import socket
import socks

# Set up the SOCKS5 proxy
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=0'

# Create a requests session and apply the proxy
session = requests.Session()
session.proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Function to check if the Tor service is running
def check_tor_service():
    try:
        sock = socket.create_connection(("127.0.0.1", 9050), timeout=5)
        sock.close()
        return True
    except (socket.error, socket.timeout):
        return False

# Function to run curl command with traffic through Tor
def run_curl_command(domain, protocol, ip):
    port = "443" if protocol == "https" else "80"
    command = f"curl --socks5 127.0.0.1:9050 --resolve '{domain}:{port}:{ip}' {protocol}://{domain}/ --max-time 10"
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        stdout = result.stdout.decode('utf-8')
        return stdout
    except subprocess.TimeoutExpired:
        return "Timeout"
    except Exception as e:
        return f"Error: {str(e)}"

def check_redirects(url, max_redirects=10):
    try:
        response = requests.get(url, allow_redirects=False)
        redirects = []
        while response.is_redirect and len(redirects) < max_redirects:
            redirects.append(response.url)
            response = requests.get(response.headers['Location'], allow_redirects=False)
        
        if len(redirects) >= max_redirects:
            print(f"Too many redirects (more than {max_redirects}):")
        else:
            print("Redirect chain:")
        
        for i, redirect in enumerate(redirects, 1):
            print(f"{i}. {redirect}")
        
        print(f"Final destination: {response.url}")
        print(f"Final status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python redirect_checker.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    check_redirects(url)
