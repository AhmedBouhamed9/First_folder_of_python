from selenium.webdriver.common.by import By
def get_products_url(driver):
    url="https://www.tunisianet.com.tn/377-telephone-portable-tunisie"
    driver.get(url)

    urls=[]
    titles=driver.find_elements(By.CLASS_NAME,"product-title")
    for title in titles:
        archon=title.find_element(By.TAG_NAME,"a")
        link=archon.get_attribute("href")
        urls.append(link)
    return urls