import os
import json
import pprint
current_folder= os.path.join(os.getcwd(),"homework")
name=input("give me the noun for search\n")

folder=os.path.join(current_folder,name+".json")
try:
    with open(folder,'r')as search:
        content=search.read()
        contact=json.loads(content)
    pprint.pprint(contact)
except FileNotFoundError:
    print ("this contact is not available you can add it")

