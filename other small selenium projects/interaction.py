from selenium import webdriver
from selenium.webdriver.common.by import By

# url = 'https://en.wikipedia.org/wiki/Main_Page'

url = 'https://secure-retreat-92358.herokuapp.com/'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url)

# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()

fname = driver.find_element(By.NAME, value='fName')
fname.send_keys("jeni")
lname = driver.find_element(By.NAME, value='lName')
lname.send_keys("Clive")
email = driver.find_element(By.NAME, value='email')
email.send_keys("jeniclieve@gmail.com")
button = driver.find_element(By.TAG_NAME, value='button')
button.click()
