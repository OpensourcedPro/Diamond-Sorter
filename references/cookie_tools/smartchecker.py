import socket
import ssl
import sys
import re

def normalize_url(url):
    try:
        # Remove http:// or https:// prefix
        url = re.sub(r'^https?://', '', url)
        parts = url.split('/', 1)
        host = parts[0]
        path = '/'
        if len(parts) > 1:
            path += parts[1]
        return host, path
    except Exception as e:
        sys.exit(f"Error normalizing URL: {e}")

def fetch_response(host, path):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as conn:
                conn.send(f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode('utf-8'))
                data = conn.recv(4096)
                response = data.decode('utf-8')
    except socket.error as e:
        sys.exit(f"Error creating connection: {e}")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}")

    try:
        search_status_code = re.search(r'\s(\d{3})\s', response)
        status_code = int(search_status_code.group(1))
    except (AttributeError, ValueError):
        sys.exit("Error parsing status code from response")

    if 300 <= status_code < 400:
        try:
            search_location = re.search(r'location: (.+)', response, re.IGNORECASE)
            if search_location is not None:
                redirect_url = search_location.group(1).strip()
                host, path = normalize_url(redirect_url)
                return fetch_response(host, path)
        except Exception as e:
            sys.exit(f"Error handling redirection: {e}")

    return response, status_code

def parse_and_print_cookies(response):
    try:
        lines = response.split('\r\n')
        cookies = []
        for line in lines:
            if line.startswith('Set-Cookie:'):
                cookie_data = line[len('Set-Cookie:'):].strip()
                parts = cookie_data.split(';')
                cookie_name = parts[0].split('=')[0].strip()
                cookie = {'name': cookie_name}
                for part in parts[1:]:
                    part = part.strip()
                    if part.lower().startswith('expires='):
                        cookie['expires'] = part[len('expires='):].strip()
                    elif part.lower().startswith('domain='):
                        cookie['domain'] = part[len('domain='):].strip()
                cookies.append(cookie)
        print("2. List of Cookies:")
        if cookies:
            for cookie in cookies:
                print(f"cookie name: {cookie['name']}", end='')
                if 'expires' in cookie:
                    print(f", expires time: {cookie['expires']}", end='')
                if 'domain' in cookie:
                    print(f"; domain name: {cookie['domain']}", end='')
                print()
        else:
            print("There are no cookies.")
    except Exception as e:
        sys.exit(f"Error parsing cookies: {e}")

def check_password_protected(status_code):
    if status_code >= 400:
        print("3. Password-protected: yes")
    else:
        print("3. Password-protected: no")

def check_http2(domain):
    context = ssl.create_default_context()
    context.set_alpn_protocols(['h2', 'http/1.1'])
    conn = None
    try:
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.connect((domain, 443))
        selected_protocol = conn.selected_alpn_protocol()
        print("1. Supports http2: yes" if selected_protocol == 'h2' else "1. Supports http2: no")
    except Exception as e:
        sys.exit(f"1. HTTP/2 (h2) Not Supported (Error: {str(e)})")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python ./smartchecker.py <url>\n\nDeveloped for DiamondSorter")
        
    try:
        url = sys.argv[1]
        host, path = normalize_url(url)
        response, status_code = fetch_response(host, path)
        print(f"website: {host}")
        check_http2(host)
        parse_and_print_cookies(response)
        check_password_protected(status_code)
    except Exception as e:
        sys.exit(f"Unexpected error: {e}")
