weibo-bigben [![Build Status](https://travis-ci.org/redswallow/weibo-bigben.svg?branch=master)](https://travis-ci.org/redswallow/weibo-bigben)
=========

### Demo
吞吞不靠谱报时 http://weibo.com/u/2344884610
 
![吞吞不靠谱报时](http://pic.yupoo.com/redswallow_v/D4ttzPEC/vXY3I.png "吞吞不靠谱报时")

### How to deploy

* Creating a Weibo Application
* Update APPKEY, APPSECRET, CALLBACKURL in config.ini
* Get Your Access Token for OAuth
* Create a new application in Google App Engine
* Download the [Google App Engine SDK](https://cloud.google.com/appengine/downloads)
* Update app.yaml
* Create lib folder: 
```shell
mkdir lib
```
* Install 3rd-party libraries to lib: 
```shell
pip install -t lib -r requirements.txt
```
* You can deploy the code easily by GoogleAppEngineLauncher. What's more, you can the command line:
```shell
python appcfg.py update [project folder]
```
