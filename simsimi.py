#-*-coding:utf-8-*-
import requests
import random
try:
    from settings import SIMSIMI_KEY
except:
    SIMSIMI_KEY = ''

class SimSimi:
    def __init__(self):
        self.session = requests.Session()
        self.chat_url = 'http://www.simsimi.com/func/req?lc=ch&msg=%s'
        self.api_url = 'http://api.simsimi.com/request.p?key=%s&lc=ch&ft=1.0&text=%s'
        if not SIMSIMI_KEY:
            self.initSimSimiCookie()

    def initSimSimiCookie(self):
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:18.0) Gecko/20100101 Firefox/18.0'})
        self.session.get('http://www.simsimi.com/talk.htm')
        self.session.headers.update({'Referer': 'http://www.simsimi.com/talk.htm'})
        self.session.get('http://www.simsimi.com/talk.htm?lc=ch')
        self.session.headers.update({'Referer': 'http://www.simsimi.com/talk.htm?lc=ch'})

    def getSimSimiResult(self, message, method='normal'):
        if method == 'normal':
            r = self.session.get(self.chat_url % message)
        else:
            url = self.api_url % (SIMSIMI_KEY, message)
            r = requests.get(url)
        return r

    def chat(self, message=''):
        if message:
            r = self.getSimSimiResult(message, 'normal' if not SIMSIMI_KEY else 'api')
            try:
                answer = r.json()['response']
                return answer
            except:
                return random.choice([u'呵呵', u'。。。', u'= =', u'=。='])
        else:
            return u'叫我干嘛'


def handle(data, bot):
    return simsimi.chat(data['message'])

if __name__ == '__main__':
    simsimi = SimSimi()
    print simsimi.chat('我还有最后一个问题')
    print simsimi.chat('我还有一个问题')
    print simsimi.chat('谁最萌')
