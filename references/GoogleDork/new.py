import os
import re
import sys
import os
import shutil
from datetime import datetime


def sort_by_services(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                service_name = os.path.splitext(file)[0]
                service_dir = os.path.join(path, service_name)
                os.makedirs(service_dir, exist_ok=True)
                with open(os.path.join(root, file), 'r') as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        line = line.strip()
                        search_user_pass(line, service_dir)


def search_user_pass(keyword, output_dir):
    for root, dirs, files in os.walk("Passwords"):
        for file in files:
            if file == "Passwords.txt":
                with open(os.path.join(root, file), 'r') as input_file:
                    for line in input_file:
                        line = line.strip()
                        if keyword in line:
                            output_file = os.path.join(output_dir, f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.txt")
                            with open(output_file, 'a') as output:
                                output.write(line + '\n')




def remove_spaces(string):
    return ''.join(ch for ch in string if not ch.isspace())

def set_console_color(color):
    if sys.platform == 'win32':
        import ctypes
        std_output_handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_output_handle, color)
    else:
        print(f"\033[{color}m", end='')

def reset_console_color():
    if sys.platform == 'win32':
        set_console_color(15)
    else:
        print("\033[0m", end='')

def search_and_save(path, keyword, save_mode):
    output_path = "results/results.txt"
    unique_entries = set()
    print("Choose the format for saving the results:")
    print("1. EMAIL:PASS")
    print("2. USER:PASS")
    save_option = int(input())
    
    with open(output_path, 'w') as output:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == "Passwords.txt":
                    with open(os.path.join(root, file), 'r') as input_file:
                        lines = input_file.readlines()
                        for i in range(len(lines)):
                            if keyword in lines[i]:
                                for j in range(i + 1, len(lines)):
                                    if "Username:" in lines[j]:
                                        username = remove_spaces(lines[j].split("Username:")[1])
                                    elif "Password:" in lines[j]:
                                        password = remove_spaces(lines[j].split("Password:")[1])
                                        if len(username) >= 3 and len(password) >= 3:
                                            is_email = '@' in username
                                            if (save_option == 1 and is_email) or (save_option == 2 and not is_email):
                                                entry = f"{username}:{password}"
                                                if username not in unique_entries and username != "UNKNOWN" and password != "UNKNOWN":
                                                    output.write(entry + '\n')
                                                    set_console_color(10)
                                                    print(entry)
                                                    reset_console_color()
                                                else:
                                                    set_console_color(12)
                                                    print(entry)
                                                    reset_console_color()
                                        break

def search_cookies(path, keyword):
    cookies_dir = "results/cookies"
    os.makedirs(cookies_dir, exist_ok=True)
    counter = 1
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "Google_[Chrome]_Default Network.txt":
                with open(os.path.join(root, file), 'r') as input_file:
                    lines = input_file.readlines()
                    if any(keyword in line for line in lines):
                        output_path = os.path.join(cookies_dir, f"{counter}.txt")
                        with open(output_path, 'w') as output:
                            output.write(os.path.join(root, file) + '\n')
                        counter += 1

def search_autofills(path, keyword):
    autofills_dir = "results/autofills"
    os.makedirs(autofills_dir, exist_ok=True)
    counter = 1
    prev_line = ""
    save = False
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and os.path.basename(root) == "Autofills":
                with open(os.path.join(root, file), 'r') as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        if keyword in line:
                            save = True
                        if "Name:" in prev_line and "Value:" in line:
                            if save:
                                output_path = os.path.join(autofills_dir, f"{counter}.txt")
                                with open(output_path, 'a') as output:
                                    output.write(prev_line + '\n')
                                    output.write(line + '\n')
                                counter += 1
                            save = False
                        prev_line = line

def search_credit_cards(path):
    cc_dir = "results/cc"
    os.makedirs(cc_dir, exist_ok=True)
    counter = 1
    cc_pattern = r"(\b(?:\d{4}[\s\-]{0,1}){3}\d{4}\b)"
    exp_pattern = r"(?:0[1-9]|1[0-2])\/?([0-9]{2})"
    cvv_pattern = r"(\b\d{3,4}\b)"
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), 'r') as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        cc_match = re.search(cc_pattern, line)
                        exp_match = re.search(exp_pattern, line)
                        cvv_match = re.search(cvv_pattern, line)
                        if cc_match and exp_match and cvv_match:
                            entry = f"CC: {cc_match.group(0)}, Expiry: {exp_match.group(0)}, CVV: {cvv_match.group(0)}"
                            output_path = os.path.join(cc_dir, f"{counter}.txt")
                            with open(output_path, 'a') as output:
                                output.write(entry + '\n')
                            counter += 1

def search_discord_tokens(path):
    discord_dir = "results/discord"
    os.makedirs(discord_dir, exist_ok=True)
    counter = 1
    token_pattern = r"^[a-zA-Z0-9._-]{24}\.[a-zA-Z0-9._-]{6}\.[a-zA-Z0-9._-]{27}$"
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and os.path.basename(root) == "Discord":
                with open(os.path.join(root, file), 'r') as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        if re.match(token_pattern, line):
                            entry = f"Token: {line.strip()}"
                            output_path = os.path.join(discord_dir, f"{counter}.txt")
                            with open(output_path, 'a') as output:
                                output.write(entry + '\n')
                            counter += 1


def main():
    print("Launching Totoware tool, make sure you have your logs ready")
    while True:
        print()
        print("[1] - Search Accounts")
        print("[2] - Search Cookies")
        print("[3] - Search Autofills")
        print("[4] - Search Credit Cards")
        print("[5] - Search FTPs")
        print("[6] - Sort Files By Date")
        print("[7] - Sort By Services")
        print("[8] - Find Discord Token")

        print("[0] - Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            print("Exiting the application.")
            break
        elif choice == 1:
            path = input("Enter the path: ")
            keyword = input("Enter the keyword: ")
            save_mode = input("Choose saving mode (email/user): ")
            search_and_save(path, keyword, save_mode)
        elif choice == 2:
            path = input("Enter the path: ")
            keyword = input("Enter the keyword (e.g., facebook.com/facebook): ")
            search_cookies(path, keyword)
        elif choice == 3:
            path = input("Enter the path: ")
            keyword = input("Enter the keyword: ")
            search_autofills(path, keyword)
        elif choice == 4:
            path = input("Enter the path: ")
            search_credit_cards(path)
        elif choice == 5:
            path = input("Enter the path: ")
            search_ftp_connections(path)
        elif choice == 6:
            path = input("Enter the path: ")
            sort_files_by_date(path)
        elif choice == 7:
            # Sort By Services
            path = "Categories"  # Path to the directory containing the category text files
            sort_by_services(path)
        elif choice == 7:
            path = input("Enter the path: ")
            search_discord_tokens(path)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()