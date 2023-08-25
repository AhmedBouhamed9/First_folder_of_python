import os
current_folder= os.path.join(os.getcwd(),"homework")
name=input("give me the noun to delete\n")

folder=os.path.join(current_folder,name+".json")
os.remove(folder)