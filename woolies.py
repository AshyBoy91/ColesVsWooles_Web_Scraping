from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def woolies_search(item:str):
    """Returns list of list with "Name", "Price", "Spec" """
    # Your path for "chromedriver". Check for correct version
    chrome_driver_path = "D:\Python learning\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    # Item to search
    item_to_lookup = f"woolworths {item}"
    driver.get(f"https://www.woolworths.com.au/")
    time.sleep(2)
    search = driver.find_element(By.ID, 'wx-headerSearch')
    search.send_keys(item_to_lookup)
    search.send_keys(Keys.ENTER)
    # Time for webpage to load in case of incomplete web page render
    time.sleep(4)
    # product_list = driver.find_element(By.ID, 'product-list')
    product_names = driver.find_elements(By.CLASS_NAME, 'shelfProductTile-description')
    name = [n.find_element(By.CLASS_NAME, 'shelfProductTile-descriptionLink').text for n in product_names]
    # prices are in one class below
    both_prices = driver.find_elements(By.CLASS_NAME, 'shelfProductTile-price')
    # prices split and combined
    priced = [n.find_element(By.CLASS_NAME, 'price-dollars').text for n in both_prices]
    pricec = [n.find_element(By.CLASS_NAME, 'price-centsPer').text.replace("\n","") for n in both_prices]
    price = [(priced[n]+pricec[n]) for n in range(len(priced))]

    price_spec = [n.text.splitlines()[3] for n in both_prices]

    listw = []
    # Add items in dictionary in case you want to make dictionary
    print(price_spec)
    # Add items in list
    for n in range(len(product_names)):

        q = [name[n]]
        w = [price[n]]
        e = [price_spec[n]]
        k = q+w+e
        listw.append(k)

    # print(listw)
    driver.quit()
    return listw
