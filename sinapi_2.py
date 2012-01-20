# -*- coding: utf-8 -*-
import urllib2
import simplejson as json
import time
from weibopy.auth import OAuthHandler
from weibopy.api import API

#config
consumer_key="222922387";consumer_secret ="9377bf8ef403aca32cd465d684fbbcaf"
#get through PIN:auth.get_authorization_url() auth.get_access_token()
token="9100f587b83fa3fae48cd93bab3981ca";tokenSecret="3f6e772d7767540fcd0bb4deb223576c"
#get_api
auth=OAuthHandler(consumer_key,consumer_secret)
auth.setToken(token, tokenSecret)
api=API(auth)
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
status = api.update_status(message)
print status.__getattribute__('id')
print "update: "+ message
