from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def coles_search(suburb:str, item:str):
    """Returns list of list with "Name", "Price", "Spec" """
    # Your path for "chromedriver". Check for correct version
    chrome_driver_path = "Your Path"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    # Item to search
    item_to_lookup = f"coles {item}"
    driver.get(f"https://shop.coles.com.au/a/{suburb}/home")
    search = driver.find_element(By.ID, 'searchTerm')
    search.send_keys(item_to_lookup)
    search.send_keys(Keys.ENTER)
    # Time for webpage to load in case of incomplete web page render
    time.sleep(2)
    # product_list = driver.find_element(By.ID, 'product-list')
    product_list = driver.find_elements(By.CLASS_NAME, 'product-main-info')
    # Create lists for name, weight/spec and price from total product list
    name = [(n.find_element(By.CLASS_NAME, 'product-brand').text +" "+ n.find_element(By.CLASS_NAME, 'product-name').text) for n in product_list]
    weighto = [n.find_element(By.CLASS_NAME, "package-size").text for n in product_list]
    price = [n.find_element(By.CLASS_NAME, 'price-container').text for n in product_list]
    dictc = {}
    listc = []
    # Add items in dictionary in case you want to make dictionary
    # for n in range(len(product_list)):
    #     dictc [n] = {
    #         "Name": name[n],
    #         "Price": price[n],
    #         "Spec": weighto[n]
    #     }
    # Add items in list
    for n in range(len(product_list)):

        q = [name[n]]
        w = [price[n]]
        e = [weighto[n]]
        k = q+w+e
        listc.append(k)

    # print(dictc)
    # print(listc)
    driver.quit()
    return listc

# coles_search(suburb="gosnells", item="water")
