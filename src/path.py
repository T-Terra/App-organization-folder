import os

# Get disc of system
disc = os.getcwd().split('\\')[0]

# Get folder user root
folder_users = os.getcwd().split('\\')[1]

# Get user of system use os.getlogin()
user = os.getlogin()

# Get destination folder
folders = ['Downloads', 'Documents', 'Desktop']

# dir default with user
main_path = f"{disc}\\{folder_users}\\{user}\\{folders[0]}"

# main_dir path to file log
path_file_log = f"{disc}\\{folder_users}\\{user}\\{folders[1]}\\Github\\App-organization-folder\\logs"

print(main_path)