import unicodedata

from utils import get_twitter_request


def post_tweet(config, tweet):
    twitter_request = get_twitter_request(config)
    url = config.get_post_tweet_url()
    payload = {
        'status': unicodedata.normalize('NFKD', tweet).encode('ascii', 'ignore')
    }
    twitter_request.post(url, params=payload)
