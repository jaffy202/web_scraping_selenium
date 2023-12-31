from twitter_bot import InternetSpeedTwitterBot


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'your_mail'
TWITTER_PASSWORD = 'your_password'
TWITTER_USERNAME = 'your_username'

twitter_complain_bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP, TWITTER_EMAIL, TWITTER_PASSWORD, TWITTER_USERNAME)
twitter_complain_bot.get_internet_speed()
twitter_complain_bot.tweet_at_provider()
