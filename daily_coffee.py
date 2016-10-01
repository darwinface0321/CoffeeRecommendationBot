#!/usr/bin/env python3.4
# Encoding: Utf-8
import random
from collections import OrderedDict, deque
import keys  # create a keys.py file with your twitter tokens if you want to run your own instance !
import logging
from TwitterAPI import TwitterAPI, TwitterRequestError
import attributes


def order():
    # order coffee in this order: (source: http://www.delish.com/food/a42014/17-secrets-of-a-starbucks-barista/)
    #   Hot or iced
    #   Size
    #   Decaf
    #   Number of shots (if any extra)
    #   Number of pumps of syrup (if you're that specific)
    #   Type of milk
    #   Any extras (mo' whip, mo' deliciousness)
    #   Drink type (latte, Frappuccino, etc.)

    order = OrderedDict()
    order[random.choice(attributes.temp)] = True
    order[random.choice(attributes.size)] = True
    for i in range(random.randint(0,5)):
        order[random.choice(attributes.attribute)] = True
    order[random.choice(attributes.multi)] = True   
    order[random.choice(attributes.syrup_type)] = True
    order[random.choice(attributes.syrup)] = True 
    order[random.choice(attributes.coffee)] = True
    for i in range(random.randint(0,2)):
        order[random.choice(attributes.appendition)] = True
    return " ".join(" ".join(order.keys()).split())


def make_tweet():
    while True:
        o = u"Coffee of the day :\n"+order()
        if len(o) < 140:
            return o

logging.info("Connecting to Twitter API")
#api = TwitterAPI(keys.consumer_key, keys.consumer_secret, keys.access_token_key, keys.access_token_secret)
#bot = api.request('account/verify_credentials').json()["screen_name"]
logging.info("Connected")
print(u"Coffee of the day :\n"+order())

# try:
#     logging.info("Sending COTD")
#     t = make_tweet()
#     r = api.request('statuses/update', {'status' : t})
#     logging.info("COTD with status : {}".format(r.status_code))
#     logging.info("Done !")
# except TwitterRequestError as e:
#     logging.exception(e)
