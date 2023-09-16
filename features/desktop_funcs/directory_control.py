import subprocess

# Open Directory
def open_directory(directory_path):
    subprocess.Popen(['explorer', directory_path])  # Open the directory using the default file explorer