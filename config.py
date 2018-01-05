import yaml


TWITTER_API_BASE_URL = 'https://api.twitter.com/1.1/'
TWITTER_API_USER_TIMELINE_ENDPOINT = 'statuses/user_timeline.json'
TWITTER_API_UPDATE_ENDPOINT = 'statuses/update.json'


class Config:
    def __init__(self):
        with open('config.yml', 'r') as config_file:
            self.config = yaml.load(config_file)

    def get_twitter_api_param(self, param):
        return self.config['twitter_api'][param]

    def get(self, param):
        return self.config[param]

    @staticmethod
    def get_tweets_url():
        return TWITTER_API_BASE_URL + TWITTER_API_USER_TIMELINE_ENDPOINT

    @staticmethod
    def get_post_tweet_url():
        return TWITTER_API_BASE_URL + TWITTER_API_UPDATE_ENDPOINT
