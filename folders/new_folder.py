import os 

parent_folder = os.getcwd()#to get the path of the parent folder
current_folder= os.path.join(parent_folder,"folders")#to get the pas of the current folder
name=input("give me a noun")
idk_folder= os.path.join(current_folder,name)
name_folder= os.path.join(parent_folder,"ahmed")
print ("the parent folder is " , parent_folder)
print ("the current folder is " , current_folder)
###create a new folder
os.mkdir(idk_folder)
try:
    os.mkdir(name_folder)
except FileExistsError:
    print("file is already exist")