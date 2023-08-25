# import math#from math import cos
# print(math.cos(30))
import json
with open(r"jsonpy\person.json",'r') as json_file :
    content= json_file.read()
    #convertion from str to dict
    person = json.loads(content)
    print(person)
    print(person["name"])