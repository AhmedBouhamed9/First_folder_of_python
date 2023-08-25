from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pprint
from get_product import get_product
from save import save_product
from get_products import get_products_url
driver = webdriver.Edge()

urls=get_products_url(driver)

for url in urls:
    product=get_product(driver,url)
    save_product(product)
    time.sleep(1)
#urls=["https://www.tunisianet.com.tn/aspirateur-tunisie-vapeur/30974-aspirateur-allume-cigare-pour-voiture-techwood-tav-8266.html",
#     "https://www.tunisianet.com.tn/telephonie-tablette/64447-tablette-galaxy-tab-s8-plus-5g-8go-128-go-gris-stylet-s-pen-.html",
#     "https://www.tunisianet.com.tn/informatique/50158-pc-portable-de-travail-dell-precision-5550-i9-10e-gen-32-go.html",
#     "https://www.tunisianet.com.tn/pc-portable-tunisie/54602-station-de-travail-mobile-dell-precision-5560-tactile-i7-11e-gen-32-go.html"]
# for url in urls:

#     product=get_product(driver,url)
#     save_product(product)
# time.sleep(1)
# driver.close()
