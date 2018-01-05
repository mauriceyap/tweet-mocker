from dateutil import parser
from datetime import datetime

from utils import get_twitter_request, OK_STATUS_CODE


def get_tweet_content(tweet):
    return tweet['full_text'].split(': http')[0].decode('utf-8')  # remove web link at end of tweet and decode unicode


def twitter_api_request(config):
    twitter_request = get_twitter_request(config)
    url = config.get_tweets_url()
    payload = {
        'screen_name': config.get('twitter_screen_name'),
        'count': config.get('est_max_tweets_in_interval'),
        'tweet_mode': 'extended'
    }

    response = twitter_request.get(url, params=payload)

    if response.status_code == OK_STATUS_CODE:
        return response.json()

    print response.raise_for_status()


def is_recent_timestamp(timestamp, interval_seconds):
    time = parser.parse(timestamp).replace(tzinfo=None)
    return (datetime.now() - time).total_seconds() <= interval_seconds


def get_recent_tweets_within_interval(config):
    recent_tweets_within_interval = [
        tweet
        for tweet in twitter_api_request(config)
        if is_recent_timestamp(tweet['created_at'], config.get('recent_interval_seconds'))]

    # No tweets in interval
    if len(recent_tweets_within_interval) == 0:
        return None

    return [get_tweet_content(tweet) for tweet in recent_tweets_within_interval]
