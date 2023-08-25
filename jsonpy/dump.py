import json
pet= {
    "cat":"mimi",
    "age":"4 mounths"
}
with open(r"jsonpy\dump.json",'w') as dump_file:
    #convertion from dict to json
    dump_pet=json.dumps(pet)
    dump_file.write(dump_pet)