import os

# Get user of system
user = os.getcwd().split('\\')[2]

# dir default with user
folder_download = f"C:\\Users\\{user}\\Downloads"