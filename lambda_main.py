from config import Config
from listener import get_recent_tweets_within_interval
from spongebob_mocking import generate_spongebob_mocking
from tweeter import post_tweet


def lambda_handler(event, context):
    config = Config()
    original_tweets = get_recent_tweets_within_interval(config)

    if original_tweets:
        new_tweets = [generate_spongebob_mocking(tweet) for tweet in original_tweets]
        map(lambda t: post_tweet(config, t), new_tweets)
