#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from weibopy.auth import OAuthHandler
from weibopy.api import API
import random

#config
consumer_key="222922387";consumer_secret ="9377bf8ef403aca32cd465d684fbbcaf"
#get through PIN:auth.get_authorization_url() auth.get_access_token()
token="9100f587b83fa3fae48cd93bab3981ca";tokenSecret="3f6e772d7767540fcd0bb4deb223576c"
#get_api
auth=OAuthHandler(consumer_key,consumer_secret)
auth.setToken(token, tokenSecret)
api=API(auth)

#get_hour
message=''
sh=time.strftime("%H", time.localtime(time.time() + 8 * 60 * 60))
h=int(sh)
for i in range(h):
    message=message+u"吞~"

if (h==7):
    message+=u" 我在清晨时候醒来(～o～)~zZ"
if (h==8):
    message+=u" 猪头,昨天又去哪里混了!(﹁\"﹁) 现在都几点了,你跟我约了,还不赶快起床!!你已经迟到了哦!!!"
if (h==9):
    message+=u" 而且你的闹钟明天开始可能就不会理你了，你的所有朋友也不会再理你了，赶快起床，赶快起床≧︿≦!!!!"
if (h==10):
    message+=u" 要不然以后如果有演唱会我不会带你去看了，有新的CD我也不会借你，然后如果有什么好看的事情我也不会再理你了，有好看的e-mail我也不会传给你了，所以快点起床(╯￣Д￣)╯摔!!!!"
if (h==11):
    message+=u" 我不要再等你啦!!!!快点!!!!!!!!!( ￣O￣)ノノ……∞∞OOO))) piu~~~"
if (h==12):
    message+=u" 我要吃掉你的坏情绪,吃掉你的坏脾气●▽●  一口一口一口一口 吃干净=口=!"
if (h==13):
    message+=u" 呆...( ° ▽、° ) 晒太阳~~"
if (h==14):
    message+=u" 民娜桑~要认真工作哦！！！"
if (h==15):
    message+=u" 额..."
if (h==16):
    message+=u" 额..."
if (h==17):
    message+=u" 额..."
if (h==18):
    message+=u" 哎呀哎呀，主人~今天晚上吃什么捏?"
if (h==19):
    message+=u" 夜已晚得很美丽~天已亮得很分明~我在你的回忆里~是黄昏还是黎明?"
if (h==21):
    message+=u" 每天的晚上，都想在你身边，看无聊的电视节目，不需要理由就这样静静靠在你怀里"
if (h==22):
    message+=u" 晚上十点以后,留给失眠的宵夜!dala~~~~~~dala~~~~~~dala~~~~~~~主人!该吃药了哟亲!!!"
if (h==23):
    message+=u" (*^・_・)23点了耶！关注我的mm们，该准备睡觉了哦！(～o～)~zZ"
if (h==0):
    message+=u" 一夜一夜熬出深深黑眼圈~这就是我爱你的表现!!!答哩啦哩啦答答 答哩啦哩啦答答 答哩啦哩啦答答~~~ 熬夜变熊猫●_●"
if (h==1):
    message+=u" 漫漫长夜 细雨点 最爱我的你 是否 沉沉入睡TT"

message=message+u" 现在是红吞吞扮演的陈萌萌附体的爱菜酱不靠谱时间"+sh+u"点整！"
#update_status
message = message.encode("utf-8")
if (h==12)or(h==18)or(h==22):
    img="img/eat"+str(random.randint(1,13))+".jpg"
    api.upload(img,message);
else:
    status = api.update_status(message)
#print status.__getattribute__('id')
#print "update: "+ message
