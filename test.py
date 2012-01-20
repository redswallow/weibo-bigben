# -*- coding: utf-8 -*-
'''
Created on 2011-8-27

@author: redswallow
'''

from tweepy.auth import OAuthHandler
from tweepy.api import API

consumer_key="o2K22DnJqSG0STjRbLUA";consumer_secret ="SV7I5YxQ8ehDCEBnKmCHYMTJW0Z0MLt3kpEdW9KhaCo"
token="25798843-PyBwBx4AWqjUuSAm9yoKQuSvEtZQR78IEsuB7xGw";tokenSecret="nWhpP3g44eciBs0Db5SXQc8HJ0G53Rd2v4sAGJy3aTU"

#get_api
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token, tokenSecret)
api=API(auth)

api.update_status(u"oauth登录成功~~")