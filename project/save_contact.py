import os
import json

parent_folder=os.getcwd()
current_folder=os.path.join(parent_folder,"project")

##get only file.json
list_of_all_folders=os.listdir(current_folder)
list_of_json_file=[]
for file in list_of_all_folders:
    if file.endswith(".json"):
        path= os.path.join(current_folder,file)
        list_of_json_file.append(path)

print (list_of_json_file)
contacts = []
for json_file in list_of_json_file:
    with open(json_file,'r')as f:
        content=f.read()
        contact= json.loads(content)
        contacts.append(contact)

print(contacts)