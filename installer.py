import nakutia

# Specify the entry point script and any additional files or directories to include
entry_point = 'diamondsorter.py'  # Replace with the actual name of your script
additional_files = ['requirements.txt']  # Add any other files or directories you want to include

# Create the installer
installer = nakutia.Installer(entry_point, additional_files=additional_files)

# Build the installer
installer.build()
