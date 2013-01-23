#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,random
from weibo import APIClient
import config,simsimi
from google.appengine.ext import db
from datastore import MessageConfig

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
    since_id = MessageConfig().all().order('-since_id').get().since_id
    print 'old since_id=%s'%since_id
    comments=client.get.comments__to_me(since_id=since_id,filter_by_author=0)

    for comment in comments['comments']:
        message=bot.chat(comment['text'])
        result=client.post.comments__reply(cid=comment['id'],id=comment['status']['id'],comment=message)
        #update since_id
        print 'new since_id=%d'%result['id']
        message_config = MessageConfig()
        message_config.since_id=result['id']
        message_config.put()
        print message
        #print 'cid=%d,id=%d' %(comment['id'],comment['status']['id'])

if __name__=='__main__':
    chatting_task()
