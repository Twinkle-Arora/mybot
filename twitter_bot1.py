import tweepy
import time

CONSUMER_KEY = '1cBOe0nCAMmVTIqP84leuMejO'
CONSUMER_SECRET = 'CJtHVSZM3rfJDcAIhLFTKpoSMPTJQH5MIdI0qbYWnt0xo4ixdL'
ACCESS_KEY = '778085117441019904-134UeSfO9OTY1DQozgau1FP6qEd12CP'
ACCESS_SECRET = 'V4j1OoFfAyzAqszhzJTo5Fa8NmFzcX9aa351eXGr3GxUx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'


def retrieve_last_seen(file_name):
    f_read = open(file_name, 'r')
    last_seen = (int(f_read.read().strip()))
    f_read.close()
    return last_seen

def store_last_seen_id(last_seen, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen))
    f_write.close()
    return

def reply():
    print('replying...')
    last_seen_id = retrieve_last_seen(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id , tweet_mode='extended')

    for m in reversed(mentions):
        print(str(m.id) + ' - ' + m.full_text)
        last_seen = m.id
        store_last_seen_id(last_seen, FILE_NAME)
        if '#happybirthday' in m.full_text.lower():
            print("found #hw")
            api.update_status('@' + m.user.screen_name + '#thankyou:)', m.id)

while True:
    reply()
    time.sleep(2)