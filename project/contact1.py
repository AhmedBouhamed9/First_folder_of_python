import json 
import os
import pprint
need=input("choose between add/view/search/update/delete contact\n")
###add
def add(a):
    parent_folder=os.getcwd()
    current_folder=os.path.join(parent_folder,"project")
    file_folder=os.path.join(current_folder,name+".json")
    with open (file_folder,'w')as contact_file:
        contact_str=json.dumps(a)
        contact_file.write(contact_str)
if need=="add":
    name=input("give me a noun\n")
    age=input("give me the age \n")
    email=input("give me the email\n")
    classe =input("give me the class\n")
    contact={
        "name":name,
        "age":age,
        "email":email,
        "class":classe
        }
    add(contact)
###view
def view():
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

    pprint.pprint(contacts)
if need=="view":
    view()
###search
def search(b):
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

    pprint.pprint(contacts)
    result={}
    for contact in contacts:
        if b in contact["name"]:
            result=contact
    print("the result is ",b)
    if (len(result)>0):
        pprint.pprint(result)
    else:
        print("not found")
if need=="search":
    
    name=input("give me the noun to search\n")
    search(name)
###update
def update(a):
    parent_folder=os.getcwd()
    current_folder=os.path.join(parent_folder,"project")

    ##get only file.json
    list_of_all_folders=os.listdir(current_folder)
    list_of_json_file=[]
    for file in list_of_all_folders:
        if file.endswith(".json"):
            path= os.path.join(current_folder,file)
            list_of_json_file.append(path)

    #print (list_of_json_file)
    contacts = []
    for json_file in list_of_json_file:
        with open(json_file,'r')as f:
            content=f.read()
            contact= json.loads(content)
            contacts.append(contact)
    result={}
    for contact in contacts:
        if a in contact["name"]:
            result=contact
    print("the result is ",a)
    if (len(result)>0):
        result["score"]=14
        path=os.path.join(current_folder,result['name']+".json")
        with open ( path,'w')as u:
            content=json.dumps(result)
            u.write(content)

    else:
        print("not found")
if need=="update":
    name=input("give me the name to update\n")
    update(name)
###delete
def delete(a):
    parent_folder=os.getcwd()
    current_folder=os.path.join(parent_folder,"project")
    path=a+".json"
    c=os.path.join(current_folder,path)
    if os.path.exists(c):
        os.remove(c)
        print(c,"has been removed")
    else:
        print("this file is unavailable")
if need=="delete":
    name=input ("give the noun you want to delete\n")
    delete(name)
