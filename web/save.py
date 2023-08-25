import json 
import os

parent_path=os.getcwd()
current_path=os.path.join(parent_path,"web")
products_folder=os.path.join(current_path,"products")
def save_product(product):
    if not os.path.exists(products_folder):
        os.mkdir(products_folder)
    product_title=product['title'].replace("/","").replace(" ","")
    products_json_file= os.path.join(products_folder,f"{product_title}.json")
    with open(products_json_file,'w')as json_file:
        products_string=json.dumps(product)
        json_file.write(products_string)
        print(f"[+]{product['title']}.json has been created")
