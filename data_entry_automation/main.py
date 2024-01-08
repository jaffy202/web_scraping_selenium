from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


form_link = 'your_form_link'
Zillow_link = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(Zillow_link)
Zillow_web_page = response.text

soup = BeautifulSoup(Zillow_web_page, 'html.parser')
prices = [element.text.split('+')[0].split('/')[0] for element in soup.find_all(
    'span', attrs={'class': 'PropertyCardWrapper__StyledPriceLine'})]
address = [element.text.strip() for element in soup.find_all('address')]
property_link = [element.get('href') for element in soup.find_all('a', attrs={'class': 'property-card-link'})]

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)
chrome_option.add_argument("--start-maximized")


driver = webdriver.Chrome(options=chrome_option)

for i in range(len(prices)):
    driver.get(form_link)
    time.sleep(3)
    input_tags = driver.find_elements(By.CSS_SELECTOR, '.whsOnd.zHQkBf')
    time.sleep(2)
    input_tags[0].send_keys(address[i])
    input_tags[1].send_keys(prices[i])
    input_tags[2].send_keys(property_link[i])
    submit_button = driver.find_element(By.CSS_SELECTOR, '.NPEfkd.RveJvd.snByac')
    submit_button.click()
    time.sleep(2)

