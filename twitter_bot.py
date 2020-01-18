import tweepy

CONSUMER_KEY = '1cBOe0nCAMmVTIqP84leuMejO'
CONSUMER_SECRET = 'CJtHVSZM3rfJDcAIhLFTKpoSMPTJQH5MIdI0qbYWnt0xo4ixdL'
ACCESS_KEY = '778085117441019904-134UeSfO9OTY1DQozgau1FP6qEd12CP'
ACCESS_SECRET = 'V4j1OoFfAyzAqszhzJTo5Fa8NmFzcX9aa351eXGr3GxUx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api  = tweepy.API(auth)

mentions = api.home_timeline()

for m in mentions:
    print(str(mentions.id) + ' - ' + mention.text)