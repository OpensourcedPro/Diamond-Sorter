import os
from colorama import Fore, Style

def display_file_tree(folder_path, indent=''):
    root_dir = os.path.basename(folder_path)
    for root, dirs, files in os.walk(folder_path):
        if root != folder_path:
            # Skip directories not part of the root path
            continue
        
        # Print current directory icon and name
        folder_icon = '├──'
        folder_color = Fore.LIGHTBLACK_EX
        if os.path.isdir(root):
            if is_archived_folder(root):
                folder_color = Fore.LIGHTBLACK_EX + Style.BRIGHT
            else:
                folder_color = Fore.RESET
        print(f"{indent}{folder_color}{folder_icon} {root_dir}/")
        
        # Print all files in the current directory with icons and color coding
        for file in files:
            file_icon = '├──'
            file_name, file_extension = os.path.splitext(file)
            color = get_file_color(file_extension)
            file_icon = get_file_icon(file_extension)
            print(f"{indent}│   {color}{file_icon} {file_name}{file_extension}")

        # Recursively call the function for each subdirectory
        for subdir in dirs:
            display_file_tree(os.path.join(root, subdir), indent + '│   ')

def get_file_color(file_extension):
    # Assign colors based on file extensions
    if file_extension == '.txt':
        return Fore.MAGENTA
    elif file_extension == '.py':
        return Fore.YELLOW
    elif file_extension == '.csv':
        return Fore.RED
    elif file_extension == '.exe':
        return Fore.CYAN
    else:
        return Style.RESET_ALL

def get_file_icon(file_extension):
    # Assign icons based on file extensions
    if file_extension == '.txt':
        return '📄'
    elif file_extension == '.py':
        return '🐍'
    elif file_extension == '.csv':
        return '📊'
    elif file_extension == '.exe':
        return '💻'
    else:
        return '📄'

def is_archived_folder(folder_path):
    # Check if the folder is an archived folder
    folder_name = os.path.basename(folder_path)
    return folder_name.endswith('.zip') or folder_name.endswith('.tar') or folder_name.endswith('.gz')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the console before displaying the file tree
clear_console()

# Prompt the user to specify a folder path
folder_path = input("Enter the folder path: ")

# Call the function to display the file tree structure
display_file_tree(folder_path)

# Display the color key
print(f"\n{Fore.MAGENTA}Text files{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Python files{Style.RESET_ALL}")
print(f"{Fore.RED}CSV files{Style.RESET_ALL}")
print(f"{Fore.CYAN}Executable files{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLACK_EX + Style.BRIGHT}Archived folders{Style.RESET_ALL}")