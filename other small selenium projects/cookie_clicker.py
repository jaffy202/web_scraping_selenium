from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ids = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory',
       'buyGrandma', 'buyCursor']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')
after_5_min = time.time() + 5*60
while time.time() < after_5_min:
    after_5_sec = time.time() + 5
    while time.time() < after_5_sec:
        cookie.click()
    money = int(driver.find_element(By.ID, 'money').text.replace(',', ''))
    product_elements = driver.find_elements(By.CSS_SELECTOR, '#store b')
    product_details = [value.text for value in product_elements]
    products = product_details[-2::-1]
    for product in products:
        cost = int(product.split('-')[1].replace(',', ''))
        if money >= cost:
            buy = driver.find_element(By.ID, ids[products.index(product)])
            buy.click()
            break
cookie_per_sec = float(driver.find_element(By.ID, 'cps').text.split(':')[1])
print(cookie_per_sec)
driver.quit()
