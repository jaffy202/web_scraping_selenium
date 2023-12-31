from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:

    def __init__(self, down, up, email, password, username):
        self.promised_down = down
        self.promised_up = up
        self.twitter_email = email
        self.twitter_password = password
        self.twitter_username = username
        self.upload_speed = 0
        self.download_speed = 0
        self.test_website = 'https://www.speedtest.net/'
        self.twitter_website = 'https://twitter.com/home'
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.driver.get(self.test_website)
        time.sleep(3)
        continue_button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        continue_button.click()
        go = self.driver.find_element(By.CLASS_NAME, value='start-text')
        go.click()
        time.sleep(60)
        self.download_speed = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
        # self.driver.close()

    def tweet_at_provider(self):
        tweet = (f'Hey Internet Provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up'
                 f' when i pay for {self.promised_down}down/{self.promised_up}up?')
        self.driver.get(self.twitter_website)
        time.sleep(5)
        input_element = self.driver.find_element(By.TAG_NAME, 'input')
        input_element.send_keys(self.twitter_email)
        input_element.send_keys(Keys.ENTER)
        # next_element = self.driver.find_elements(By.TAG_NAME, 'span')[9]
        # next_element.click()
        time.sleep(5)
        try:
            pass_element = self.driver.find_element(By.NAME, 'password')
        except Exception:
            username_element = self.driver.find_element(By.TAG_NAME, "input")
            username_element.send_keys(self.twitter_username)
            username_element.send_keys(Keys.ENTER)
            time.sleep(5)
            pass_element = self.driver.find_element(By.NAME, 'password')
        finally:
            pass_element.send_keys(self.twitter_password)
            pass_element.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_element = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        tweet_element.send_keys(tweet)
        time.sleep(5)
        post_element = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                          'div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]'
                                                          '/div[2]/div/div/div/div[3]/div/span/span')
        post_element.click()
