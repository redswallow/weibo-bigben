from weibo import APIClient

APP_KEY = '1037673549' # app key
APP_SECRET = '79c0a909c1a9a48c882e6cde07fdc230' # app secret
CALLBACK_URL = 'http://www.example.com/callback' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
code = 'acea5bfeb04ca56da6e4e54711e1c30f'
r={'access_token': u'2.00WbtgYCJSyNIB378e4f5ca1vnGxAD', 'expires': 1515254019, 'expires_in': 1515254019, 'uid': u'2344884610'}
access_token = u'2.00WbtgYCJSyNIB378e4f5ca1vnGxAD'#r.access_token 
expires_in = 1515254019#r.expires_in 
client.set_access_token(access_token, expires_in)

print client.post.statuses__update(status=u'test2',pic=open('meng.jpg'))
