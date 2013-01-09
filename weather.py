#!/usr/bin/python
# -*- coding: utf-8 -*-
from weibo import APIClient
import urllib2
import simplejson as json
import time

#config
APP_KEY = '1037673549' # app key
APP_SECRET = '79c0a909c1a9a48c882e6cde07fdc230' # app secret
CALLBACK_URL = 'http://www.example.com/callback' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
code = 'acea5bfeb04ca56da6e4e54711e1c30f'
r={'access_token': u'2.00WbtgYCJSyNIB378e4f5ca1vnGxAD', 'expires': 1515254019, 'expires_in': 1515254019, 'uid': u'2344884610'}
access_token = u'2.00WbtgYCJSyNIB378e4f5ca1vnGxAD'#r.access_token 
expires_in = 1515254019#r.expires_in 
client.set_access_token(access_token, expires_in)

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
