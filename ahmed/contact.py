import json
need=input("add_contact or view or delete or search or update\n")
if need == "add_contact":



    name= input ("add the name of the new contact \n")
    number=input ("add the number of the new contact \n")
    email= input ("add the email of the new contact \n")
    contact ={name:{
        "name":name,
        "number":number,
        "email":email
    }}

    new_contact= open (r"ahmed\contact.json",'a')
    addcontact=json.dumps(contact)
    addcontact1=(addcontact+"\n")
    new_contact.write(addcontact1)

elif need == "view":
    try:
        with open(r"ahmed\contact.json",'r')as view_contact:
            content=view_contact.read()
            print(content)
    except:
        print("your contact memory is empty")
elif need == "search":
    try:
        name=input("give me a noun\n")    
        with open(r"ahmed\contact.json",'r')as search_contact:
            content=search_contact.read()
            person = json.loads(content)
            print(person[name])
    except:
        print("this is noun is unavailable you can add it") 
elif need == "update":