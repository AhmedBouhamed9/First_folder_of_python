from selenium.webdriver.common.by import By
def get_product(driver,url):
    product={}
    
    driver.get(url)
    title_element=driver.find_element(By.CLASS_NAME, "h1")
    title=title_element.text
    product["title"]=title
    reference_element=driver.find_element(By.CLASS_NAME, "product-reference")
    reference=reference_element.text
    product["reference"]=reference
    descr=driver.find_element(By.CLASS_NAME, "prodes")
    descreption= descr.text
    product["descreption"]=descreption
    price_element=driver.find_element(By.CLASS_NAME, "current-price")
    price = price_element.text
    product["price"]=price
    av=driver.find_element(By.ID, "stock_availability")
    availability=av.text
    product["availability"]=availability
    all_images=driver.find_elements(By.TAG_NAME, "img")
    image=all_images[1].get_attribute("src")
    product["image"]=image
    brand=driver.find_element(By.CLASS_NAME, "manufacturer-logo")
    brand_image=brand.get_attribute("src")
    product["brand_image"]=brand_image
    return product