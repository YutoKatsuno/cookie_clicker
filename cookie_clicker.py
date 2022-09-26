from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "/Users/katsunoyuutou/Development/chromedriver"
chrome_service = service.Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get(URL)
cookie = driver.find_element(By.ID, "cookie")
count = driver.find_element(By.ID, "money")
options = driver.find_elements(By.CLASS_NAME, "grayed")


timeout = time.time() + 60*5
buy = time.time() + 5
while True:
    num = count.text.split(",")
    cookie_num = int("".join(num))
    cookie.click()
    if time.time() > timeout:
        break
    else:
        if time.time() > buy:
            if 15 <= cookie_num < 100:
                cursor = driver.find_element(By.ID, "buyCursor")
                cursor.click()
            if 100 <= cookie_num < 500:
                grandma = driver.find_element(By.ID, "buyGrandma")
                grandma.click()
            if 500 <= cookie_num < 2000:
                factory = driver.find_element(By.ID, "buyFactory")
                factory.click()
            if 2000 <= cookie_num < 7000:
                mine = driver.find_element(By.ID, "buyMine")
                mine.click()
            if 7000 <= cookie_num < 50000:
                shipment = driver.find_element(By.ID, "buyShipment")
                shipment.click()
            if 50000 <= cookie_num < 1000000:
                alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
                alchemy_lab.click()
            if 1000000 <= cookie_num < 123456789:
                portal = driver.find_element(By.ID, "buyPortal")
                portal.click()
            if 123456789 <= cookie_num:
                time_machine = driver.find_element(By.ID, "buyTime machine")
                time_machine.click()
            buy = time.time() + 5

