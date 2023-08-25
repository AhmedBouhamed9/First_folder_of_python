import os
import json
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
parent_folder=os.getcwd()
current_folder=os.path.join(parent_folder,"project")
file_folder=os.path.join(current_folder,"ahmed.json")
with open (file_folder,'w')as contact_file:
    contact_str=json.dumps(contact)
    contact_file.write(contact_str)
