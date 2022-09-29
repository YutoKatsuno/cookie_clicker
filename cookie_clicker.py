from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import time
import os

# Get environment variable
DRIVE_PATH = os.environ["DRIVE_PATH"]

# Initializing selenium
URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = DRIVE_PATH
chrome_service = service.Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)

# Get cookie
cookie = driver.find_element(By.ID, "cookie")
count = driver.find_element(By.ID, "money")

# Get store's information
products = driver.find_elements(By.CSS_SELECTOR, "#store div")
product_ids = [product.get_attribute("id") for product in products]

# Get time
timeout = time.time() + 60 * 5
buy = time.time() + 5

is_on = True
while is_on:
    cookie.click()

    # Every 5 seconds
    if time.time() > buy:

        # Get price
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        price_list = []

        # Convert to int
        for price in prices[:8]:
            str_price = price.text
            if str_price != "":
                int_price = int(str_price.split("-")[1].strip().replace(",", ""))
                price_list.append(int_price)

        # Associate price with id
        product_dict = {}
        for n in range(len(price_list)):
            product_dict[price_list[n]] = product_ids[n]

        # Get current cookie count
        cookie_count = driver.find_element(By.ID, "money").text
        if "," in cookie_count:
            cookie_count = cookie_count.replace(",", "")
        cookie_count = int(cookie_count)

        # When I  will buy something
        for cost, product_id in product_dict.items():
            if cookie_count > cost:
                highest_product_id = product_id
        result = driver.find_element(By.ID, highest_product_id)
        result.click()

        # reset time.time()
        buy = time.time() + 5

    # After 5 minutes
    if time.time() > timeout:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
        is_on = False
        break

if not is_on:
    driver.quit()
