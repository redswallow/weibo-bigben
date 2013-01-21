#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from weibo import APIClient
import random,simplejson as json
import config,simsimi

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#config
c=config.Config()
#init api client
client = APIClient(app_key=c.app["app_key"], app_secret=c.app["app_secret"], redirect_uri=c.app["callback_url"])
client.set_access_token(c.token["access_token"], c.token["expires_in"])

message=''
bot = simsimi.SimSimi()
def chatting_task():
    print 'old since_id=%s'%c.message['since_id']
    comments=client.get.comments__mentions(since_id=c.message['since_id'],filter_by_author=0)

    for comment in comments['comments']:
        try:
            for words in comment['text'].split():
                if '@' not in words:
                    print words
                    message=bot.chat(words)
                    result=client.post.comments__reply(cid=comment['id'],id=comment['status']['id'],comment=message)
                    #update since_id
                    print 'new since_id=%d'%result['id']
                    c.update_since_id(result['id'])
                    print message
            print 'cid=%d,id=%d' %(comment['id'],comment['status']['id'])
        except:
            pass

if __name__=='__main__':
    chatting_task()
