# Window modules
import tkinter
from tkinter import messagebox
import customtkinter

# System modules
import sys
import hashlib

# Misc
import webbrowser
from authentication import *

if sys.version_info.minor < 10:  # Python version check (Bypass Patch)
    print("[Security] - Python 3.10 or higher is recommended. The bypass will not work on 3.10+")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))

if platform.system() == 'Windows':
    os.system('cls & title Python Example')  # clear console, change title
elif platform.system() == 'Linux':
    os.system('clear')  # clear console
    sys.stdout.write("\x1b]0;Python Example\x07")  # change title
elif platform.system() == 'Darwin':
    os.system("clear && printf '\e[3J'")  # clear console
    os.system('''echo - n - e "\033]0;Python Example\007"''')  # change title

print("Initializing")


#Keyauth shinanigans
def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

#Keyauth shinanigans
keyauthapp = api(
    name = "Diamond",
    ownerid = "VwOq0EhmEw",
    secret = "9406239bcd65ad50ae4f50a6dc8cfeb37fed8df164c052b13a3aa960672edf77",
    version = "1.0",
    hash_to_check = getchecksum()
)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#Create Window
app = customtkinter.CTk()
app.geometry("600x440")
app.title('Diamond Sorter Loader')

#Check license
def button_function():
    key = entry1.get()  # Get input field value
    print(key)  # Remove this for production
    tkinter.messagebox.showinfo(title="Loader", message="Your key has been processed")  # Message box
    keyauthapp.license(key)  # Check license key with keyauth
    print("AUTHENTICATION SUCCESS")
    
    # Close the Tkinter GUI
    app.destroy()
    
    # Open DiamondSorter.py
    os.system('python3 DiamondSorter.py')

    

# Open key site
def get_key():
    webbrowser.open_new_tab('license.html')

l1=customtkinter.CTkLabel(master=app)
l1.pack(fill="both", expand=True)

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=250, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#Text at top
l2=customtkinter.CTkLabel(master=frame, text="Sign in with license",font=('Century Gothic',20))
l2.place(x=50, y=45)

# Input field
entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=90)

#Get key button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Get Key", command=get_key, corner_radius=6)
button1.place(x=50, y=140)

# Login button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=180)

#Loop
app.mainloop()