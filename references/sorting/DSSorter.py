import os
import re
from pathlib import Path

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "results")
os.makedirs(output_dir, exist_ok=True)  # Create the 'results' directory if it doesn't exist

def set_console_color(color):
    if os.name == "nt":
        import ctypes
        STD_OUTPUT_HANDLE = -11
        console_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetConsoleTextAttribute(console_handle, color)
    else:
        print(f"\033[{color}m", end="")

def reset_console_color():
    if os.name == "nt":
        set_console_color(15)
    else:
        print("\033[0m", end="")

def search_and_save(path, keyword, save_mode):
    output_file = os.path.join(output_dir, "diamondsorter.results.txt")
    with open(output_file, 'w', encoding='utf-8') as output:
        save_option = int(input("Choose the format for saving the results:\n1. EMAIL:PASS\n2. USER:PASS\n"))
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == "Passwords.txt":
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as input_file:
                        lines = input_file.readlines()
                        for i in range(len(lines)):
                            if keyword in lines[i]:
                                for j in range(i+1, len(lines)):
                                    if "Username:" in lines[j]:
                                        username = remove_spaces(lines[j].split("Username:")[1])
                                    elif "Password:" in lines[j]:
                                        password = remove_spaces(lines[j].split("Password:")[1])
                                        if len(username) >= 3 and len(password) >= 3:
                                            is_email = "@" in username
                                            if (save_option == 1 and is_email) or (save_option == 2 and not is_email):
                                                entry = f"{username}:{password}"
                                                set_console_color(10)
                                                print(entry)
                                                reset_console_color()
                                                output.write(entry + "\n")
                                            else:
                                                set_console_color(12)
                                                print(entry)
                                                reset_console_color()
                                        break

def search_cookies(path, keyword):
    counter = 0  # Initialize the counter
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "Google_[Chrome]_Default Network.txt":
                with open(os.path.join(root, file), "r") as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        if keyword in line:
                            output_subdir = os.path.join(output_dir, "cookies")
                            os.makedirs(output_subdir, exist_ok=True)
                            output_file = os.path.join(output_subdir, f"{counter}.txt")
                            with open(output_file, "w", encoding='utf-8') as output:
                                output.write(os.path.join(root, file) + "\n")
                            counter += 1  # Increment the counter for each hit
    print(f"Diamond Sorter - Number of hits: {counter}")  # Display the total number of hits

def search_autofills(path, keyword):
    counter = 1
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and os.path.basename(os.path.dirname(root)) == "Autofills":
                with open(os.path.join(root, file), "r") as input_file:
                    lines = input_file.readlines()
                    save = False
                    for i in range(len(lines)):
                        if keyword in lines[i]:
                            save = True
                        if "Name:" in lines[i-1] and "Value:" in lines[i]:
                            if save:
                                output_subdir = os.path.join(output_dir, "autofills")
                                os.makedirs(output_subdir, exist_ok=True)
                                output_file = os.path.join(output_subdir, f"{counter}.txt")
                                with open(output_file, "a") as output:
                                    output.write(lines[i-1] + lines[i])
                                counter += 1
                            save = False

def sort_files_by_date(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(os.path.join(path, file))
    files.sort(key=os.path.getmtime)
    return files

def search_ftp_connections(path):
    counter = 1
    ftp_pattern = re.compile(r"ftp:\/\/(?:\w+\:\w+@)?[\w.-]+(?:\:\d+)?(?:\/.*)?", re.IGNORECASE)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        if re.search(ftp_pattern, line):
                            output_subdir = os.path.join(output_dir, "ftp")
                            os.makedirs(output_subdir, exist_ok=True)
                            output_file = os.path.join(output_subdir, f"{counter}.txt")
                            with open(output_file, "a") as output:
                                output.write(line)
                            counter += 1

def search_credit_cards(path):
    counter = 1
    cc_pattern = re.compile(r"(\b(?:\d{4}[\s\-]{0,1}){3}\d{4}\b)")
    exp_pattern = re.compile(r"(?:0[1-9]|1[0-2])\/?([0-9]{2})")
    cvv_pattern = re.compile(r"(\b\d{3,4}\b)")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        cc_match = re.search(cc_pattern, line)
                        exp_match = re.search(exp_pattern, line)
                        cvv_match = re.search(cvv_pattern, line)
                        if cc_match and exp_match and cvv_match:
                            output_subdir = os.path.join(output_dir, "cc")
                            os.makedirs(output_subdir, exist_ok=True)
                            output_file = os.path.join(output_subdir, f"{counter}.txt")
                            with open(output_file, "a") as output:
                                output.write(f"Diamond Sorter - CC: {cc_match[0]}, Diamond Sorter - Expiry: {exp_match[0]}, Diamond Sorter - CVV: {cvv_match[0]}\n")
                            counter += 1

def search_discord_tokens(path):
    counter = 1
    token_pattern = re.compile(r"^[a-zA-Z0-9._-]{24}\.[a-zA-Z0-9._-]{6}\.[a-zA-Z0-9._-]{27}$")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and os.path.basename(os.path.dirname(root)) == "Discord":
                with open(os.path.join(root, file), "r") as input_file:
                    lines = input_file.readlines()
                    for line in lines:
                        if re.search(token_pattern, line):
                            output_subdir = os.path.join(output_dir, "discord")
                            os.makedirs(output_subdir, exist_ok=True)
                            output_file = os.path.join(output_subdir, f"{counter}.txt")
                            with open(output_file, "a") as output:
                                output.write(f"Token: {line}")
                            counter += 1

def main():
    choice = 0
    path = ""
    keyword = ""
    print("Launching Diamond Sorter - Free tool, make sure you have your logs ready. Check us out @DiamondSorter on telegram")
    while choice != 0:
        os.system("cls" if os.name == "nt" else "clear")
        print("[1] - Search Accounts")
        print("[2] - Search Cookies")
        print("[3] - Search Autofills")
        print("[4] - Search Credit Cards")
        print("[5] - Search FTPs")
        print("[6] - Sort Files By Date")
        print("[7] - Find Discord Token")
        print("[0] - Exit")
        choice = int(input("Enter your choice: "))
        save_mode = ""
        if choice == 1:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            keyword = input("Enter the keyword: ")
            while save_mode != "email" and save_mode != "user":
                save_mode = input("Choose saving mode (email/user): ")
                if save_mode != "email" and save_mode != "user":
                    print("Invalid choice. Please enter either 'email' or 'user'.")
            search_and_save(path, keyword, save_mode)
        elif choice == 2:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            keyword = input("Enter the keyword (e.g., facebook.com/facebook): ")
            search_cookies(path, keyword)
        elif choice == 3:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            keyword = input("Enter the keyword: ")
            search_autofills(path, keyword)
        elif choice == 4:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            search_credit_cards(path)
        elif choice == 5:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            search_ftp_connections(path)
        elif choice == 6:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            sort_files_by_date(path)
        elif choice == 7:
            path = input("Enter the path: ")
            if not os.path.isdir(path):
                print("Invalid path selected. Please try again.")
                continue
            search_discord_tokens(path)
        elif choice == 0:
            print("Exiting the application.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()