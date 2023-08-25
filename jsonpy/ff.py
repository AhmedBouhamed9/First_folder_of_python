import os
current_folder= os.path.join(os.getcwd(),"jsonpy")
name=input("give me the noun for search\n")

folder=os.path.join(current_folder,name+".json")
os.remove(folder)