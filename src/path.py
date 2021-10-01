import os

# Get disc of system
disc = os.getcwd().split('\\')[0]

# Get folder user root
folder_users = os.getcwd().split('\\')[1]

# Get user of system
user = os.getcwd().split('\\')[2]

# Get destination folder
folders = ['Downloads', 'Documents', 'Desktop']

# dir default with user
main_path = f"{disc}\\{folder_users}\\{user}\\{folders[0]}"

print(main_path)