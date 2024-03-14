from cx_Freeze import setup, Executable

setup(
    name="DiamondSorter",
    version="1.8.7",
    description="Opensourced.Pro Project for Malware Logs",
    executables=[Executable("merged_example.py")],
)