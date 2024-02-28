from PyQt5 import uic

# Load the UI file
ui_file = "LoginCheked_UI.ui"
py_file = "LoginCheked_UI.py"

# Convert the UI file to a Python file
uic.compileUi(ui_file, open(py_file, "w"))

print(f"Successfully converted {ui_file} to {py_file}")