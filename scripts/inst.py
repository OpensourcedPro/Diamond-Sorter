import sqlite3
from getpass import getpass
from tkinter import Tk, Label, Entry, Button, messagebox
import wmi

def get_hwid():
    c = wmi.WMI()
    return c.Win32_ComputerSystemProduct()[0].UUID

# Create a database connection
conn = sqlite3.connect('user_registration.db')
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    is_admin INTEGER NOT NULL DEFAULT 0,
                    is_active INTEGER NOT NULL DEFAULT 1,
                    ip_address TEXT,
                    hwid TEXT
                )''')
conn.commit()

# Function to register a new user
def register_user():
    def register():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Check if username already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE username=?", (username,))
        if cursor.fetchone()[0] > 0:
            messagebox.showerror("Error", "Username already exists.")
            return

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully.")
        register_window.destroy()

    register_window = Tk()
    register_window.title("User Registration")
    register_window.geometry("400x200")
    register_window.resizable(False, False)

    username_label = Label(register_window, text="Username:")
    username_label.pack()
    username_entry = Entry(register_window)
    username_entry.pack()

    password_label = Label(register_window, text="Password:")
    password_label.pack()
    password_entry = Entry(register_window, show="*")
    password_entry.pack()

    confirm_password_label = Label(register_window, text="Confirm Password:")
    confirm_password_label.pack()
    confirm_password_entry = Entry(register_window, show="*")
    confirm_password_entry.pack()

    register_button = Button(register_window, text="Register", command=register)
    register_button.pack()

    register_window.mainloop()

# Function to login as admin
def admin_login():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the provided credentials are correct
        cursor.execute("SELECT COUNT(*) FROM users WHERE username=? AND password=? AND is_admin=1", (username, password))
        if cursor.fetchone()[0] > 0:
            admin_menu()
            login_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid admin credentials.")

    login_window = Tk()
    login_window.title("Admin Login")
    login_window.geometry("400x200")
    login_window.resizable(False, False)

    username_label = Label(login_window, text="Username:")
    username_label.pack()
    username_entry = Entry(login_window)
    username_entry.pack()

    password_label = Label(login_window, text="Password:")
    password_label.pack()
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    login_button = Button(login_window, text="Login", command=login)
    login_button.pack()

    login_window.mainloop()

# Function to display registered users
def show_registered_users():
    # Fetch all users from the database
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    user_list = "Registered Users:\n"
    for user in users:
        user_list += f"ID: {user[0]}, Username: {user[1]}, Active: {user[4]}, IP Address: {user[5]}, HWID: {user[6]}\n"

    messagebox.showinfo("Registered Users", user_list)

# Admin Menu
def admin_menu():
    def generate_invite_keys():
        def generate():
            num_keys = int(num_keys_entry.get())

            # Generate and insert invite keys into the database
            for _ in range(num_keys):
                invite_key = generate_random_key()  # Implement your own function to generate the invite key
                cursor.execute("INSERT INTO invite_keys (key) VALUES (?)", (invite_key,))
            conn.commit()
            messagebox.showinfo("Success", f"{num_keys} invite keys generated successfully.")
            generate_keys_window.destroy()

        generate_keys_window = Tk()
        generate_keys_window.title("Generate Invite Keys")
        generate_keys_window.geometry("400x200")
        generate_keys_window.resizable(False, False)

        num_keys_label = Label(generate_keys_window, text="Number of Invite Keys:")
        num_keys_label.pack()
        num_keys_entry = Entry(generate_keys_window)
        num_keys_entry.pack()

        generate_button = Button(generate_keys_window, text="Generate", command=generate)
        generate_button.pack()

        generate_keys_window.mainloop()

    admin_menu = Tk()
    admin_menu.title("Admin Menu")
    admin_menu.geometry("400x200")
    admin_menu.resizable(False, False)

    generate_keys_button = Button(admin_menu, text="Generate Invite Keys", command=generate_invite_keys)
    generate_keys_button.pack()

    show_users_button = Button(admin_menu, text="Show Registered Users", command=show_registered_users)
    show_users_button.pack()

    admin_menu.mainloop()

# User Menu
def user_menu():
    def login():
        def login_user():
            username = username_entry.get()
            password = password_entry.get()

            # Check if the provided credentials are correct
            cursor.execute("SELECT COUNT(*) FROM users WHERE username=? AND password=? AND is_active=1", (username, password))
            if cursor.fetchone()[0] > 0:
                messagebox.showinfo("Success", "Login successful.")
                user_menu_window.destroy()
                # Perform user actions here
            else:
                messagebox.showerror("Error", "Invalid credentials.")

        login_window = Tk()
        login_window.title("User Login")
        login_window.geometry("400x200")
        login_window.resizable(False, False)

        username_label = Label(login_window, text="Username:")
        username_label.pack()
        username_entry = Entry(login_window)
        username_entry.pack()

        password_label = Label(login_window, text="Password:")
        password_label.pack()
        password_entry = Entry(login_window, show="*")
        password_entry.pack()

        login_button = Button(login_window, text="Login", command=login_user)
        login_button.pack()

        login_window.mainloop()

    def register():
        register_user()

    user_menu_window = Tk()
    user_menu_window.title("User Menu")
    user_menu_window.geometry("400x200")
    user_menu_window.resizable(False, False)

    login_button = Button(user_menu_window, text="Login", command=login)
    login_button.pack()

    register_button = Button(user_menu_window, text="Register", command=register)
    register_button.pack()

    user_menu_window.mainloop()

# Start the user registration system
def main():
    main_window = Tk()
    main_window.title("User Registration System")
    main_window.geometry("800x600")

    # Add background image
    # Implement your own code to add a background image

    user_menu_button = Button(main_window, text="User Menu", command=user_menu)
    user_menu_button.pack()

    admin_login_button = Button(main_window, text="Admin Login", command=admin_login)
    admin_login_button.pack()

    main_window.mainloop()

if __name__ == "__main__":
    main()