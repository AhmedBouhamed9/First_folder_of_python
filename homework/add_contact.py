import json
import os
name=input("give me the noun\n")
age=input ("give me the age \n")
number=input ("give me the number\n")
email=input("give me the email\n")
contact={
    "name":name,
    "age":age,
    "number":number,
    "email":email
}
current_folder= os.path.join(os.getcwd(),"homework")
file_folder= os.path.join(current_folder,name+".json")
with open(file_folder,'w') as add_contact:
    content=json.dumps(contact)
    add_contact.write(content)