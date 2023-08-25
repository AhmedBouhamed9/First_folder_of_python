import json
import os 
current_folder= os.path.join(os.getcwd(),"homework")
name=input("give me the noun for search\n")

folder=os.path.join(current_folder,name+".json")
try:
    with open(folder,'r')as search:
        content=search.read()
        contact=json.loads(content)
    print("this is the contact now before update",contact)

    
    new_name=input("give me the new noun\n")
    new_age=input("give me the new age\n")
    new_number=input("give me the new number\n")
    new_email=input("give me the new email\n")
    contact={
        "name":new_name,
        "age":new_age,
        "number":new_number,
        "email":new_email
    }
    with open(folder,'w')as update:
        content=json.dumps(contact)
        update.write(content)
    new_folder=os.path.join(current_folder,new_name+(".json"))
    os.renames(folder,new_folder)
except FileNotFoundError:
    print ("this contact is not available you can add it")
