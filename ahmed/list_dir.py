import os
parent_folder=os.getcwd()
list_folders=os.listdir(parent_folder)
print(list_folders)
for file in list_folders:
    print(file)