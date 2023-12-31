from selenium import webdriver
from selenium.webdriver.common.by import By

# URL = 'https://www.meesho.com/rudraa-womens-coral-crepe-solid-stylish-with-belt-dress/p/4zyca'

url = 'https://www.python.org/'

# to keep the Chrome browser open even after the program finished execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

date_elements = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li time')
event_dates = [value.text for value in date_elements]


name_elements = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
event_names = [value.text for value in name_elements]

upcoming_events = {i: {'time': event_dates[i], 'name': event_names[i]} for i in range(5)}
print(upcoming_events)
# price_rupee = driver.find_element(By.TAG_NAME, 'h4').text
# print(f'The price is {price_rupee}')


# close a particular tab
# driver.close()
# close the browser
driver.quit()
