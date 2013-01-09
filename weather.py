#!/usr/bin/python
# -*- coding: utf-8 -*-
from weibo import APIClient
import urllib2
import simplejson as json
import time
import config

#config
c=config.Config()
#init api client
client = APIClient(app_key=c.app["app_key"], app_secret=c.app["app_secret"], redirect_uri=c.app["callback_url"])
client.set_access_token(c.token["access_token"], c.token["expires_in"])

#get_weather
citycode='101020100'
url='http://m.weather.com.cn/data/'+citycode+'.html'
strData=urllib2.urlopen(url).read()
data=json.loads(strData)[u'weatherinfo']

week=int(time.strftime('%w',time.localtime()))
weeks=(u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日')
date=time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 60 * 60))
message=u'吞吞robot不靠谱地提醒您，明天是'+date+','+weeks[week]+','\
+data[u'city']+u'天气'+data[u'weather2']+','+data[u'temp2']+','+data[u'wind2']+'~'+data[u'index_d']
#update_status
message = message.encode("utf-8")
client.post.statuses__update(status=message)
