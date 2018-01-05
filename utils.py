from requests_oauthlib import OAuth1Session

OK_STATUS_CODE = 200


def get_twitter_request(config):
    return OAuth1Session(config.get_twitter_api_param('consumer_key'),
                         client_secret=config.get_twitter_api_param('consumer_secret'),
                         resource_owner_key=config.get_twitter_api_param('access_token'),
                         resource_owner_secret=config.get_twitter_api_param('token_secret'))
