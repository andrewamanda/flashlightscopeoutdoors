# Create your views here.

from django.utils.html import strip_tags
from ecomstore.localsettings import *
import twitter

def updateTwitter( message ):
 
    try:
        api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET, access_token_key=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET )
        data = strip_tags(message)
        if len(data) > 140:
            data = data[:136] + '...'

        api.PostUpdate(data)
        updated = True
        #statuses = api.GetUserTimeline()[0:5] # reload the statuses
    except NameError as e:
        print ("unable to login")
        updated = False
    print ("Updated = {}".format(updated))
    return updated

