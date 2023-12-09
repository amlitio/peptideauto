import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def twitter_api():
    auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth)

def post_to_twitter(api, message):
    try:
        api.update_status(message)
    except tweepy.TweepyException as e:
        print("An error occurred while posting to Twitter: " + str(e))

def get_tweet_performance(api, tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        return {"retweets": tweet.retweet_count, "likes": tweet.favorite_count}
    except tweepy.TweepyException as e:
        print("An error occurred while fetching tweet performance: " + str(e))
        return {}

# Example usage
# api = twitter_api()
# post_to_twitter(api, "Exciting new insights in peptide research!")
# performance = get_tweet_performance(api, 'tweet_id_here')
