#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from weibo import APIClient
import random
import config

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#config
c=config.Config()
#init api client
client = APIClient(app_key=c.app["app_key"], app_secret=c.app["app_secret"], redirect_uri=c.app["callback_url"])
client.set_access_token(c.token["access_token"], c.token["expires_in"])

message=''
#get_hour
sh=time.strftime("%H", time.localtime(time.time() + int(c.time['timezone']) * 60 * 60))
h=int(sh)
#create message
for i in xrange(h):
    message=message+u"吞~"
message+=c.message[sh]
message=message+c.message['clock']%(sh)
#update_status
if sh in set(c.time['pictime'].split('|')):
    img=c.img['imgpath'] %(str(random.randint(1,int(c.img['imgnum']))))
    f=open(img,'rb')
    try:
        client.upload.statuses__upload(status=message,pic=f)
    except:
        client.post.statuses__update(status=message)
    f.close()
else:
    client.post.statuses__update(status=message)
    print message
