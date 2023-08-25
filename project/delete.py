import os
import json

parent_folder=os.getcwd()
current_folder=os.path.join(parent_folder,"project")
name=(input("give me the noun to delete \n"))
path=name+".json"
c=os.path.join(current_folder,path)
if os.path.exists(c):
    os.remove(c)
    print(c,"has been removed")
else:
    print("this file is unavailable")