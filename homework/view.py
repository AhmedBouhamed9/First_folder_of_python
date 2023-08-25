import json
import os 
import pprint
current_folder= os.path.join(os.getcwd(),"homework")
list_folder= os.listdir(current_folder)
list_files=[]
for file in list_folder:
    if file.endswith(".json"):
        path=os.path.join(current_folder,file)
        list_files.append(path)
contacts=[]
for contact in list_files:
    with open(contact,'r') as r:
        content=r.read()
        s=json.loads(content)
        contacts.append(s)
pprint.pprint(contacts)