import os
import json
import pprint
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


search_input=input("what are you searching for \n")
result={}
for contact in contacts:
    if search_input in contact["name"]:
        result=contact
print("the result is ",search_input)
if (len(result)>0):
    result["score"]=14
    path=os.path.join(current_folder,result['name']+".json")
    with open ( path,'w')as u:
        content=json.dumps(result)
        u.write(content)

else:
    print("not found")