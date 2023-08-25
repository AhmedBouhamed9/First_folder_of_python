import os
import json
working_directly= os.getcwd()
print(working_directly)
currentt=os.path.join(working_directly,"ahmed")
os_folder_exist= os.path.exists(currentt)
if(not os_folder_exist):
    os.mkdir(currentt)
curren=os.path.join(currentt,"data.json")

data={
    "name":"ahmed",
    "age":16
}
with open(curren,'w')as file_json:
    json_content=json.dumps(data)
    file_json.write(json_content)
with open(curren,'r')as json_file:
    content=json_file.read()
    data=json.loads(content)
    print(data)