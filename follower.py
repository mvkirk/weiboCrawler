#encoding:utf-8
from bs4 import BeautifulSoup 
import urllib2,cookielib,urllib,json,sys,time,re,threading

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('User-agent','Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')]
urllib2.install_opener(opener)

def query(url):
	request=urllib2.urlopen(url)
	html=request.read()
	html=html.replace('\n',' ')
	data=json.loads(html)
	return data



class timer(threading.Thread):
	url=""
	def __init__(self,url):
		threading.Thread.__init__(self)
		self.url=url
	
	def run(self):	
		time1=time.time()
		data=query(self.url)
		time2=time.time()
		print time2-time1
		for j in xrange(10):
			try:
				user=data['cards'][0]['card_group'][j]
				uid=user['user']['id']
				print uid
			except:
				pass


containerId='1005055587464347'
user_url="http://m.weibo.cn/page/json?containerid="+containerId+"_-_FOLLOWERS"

data=query(user_url)
formated=json.dumps(data,indent=4)

f=open('response.txt','w')
f.write(formated.decode('unicode-escape').encode('utf-8'))
count=data['count']

page_count=(count-1)/10+1
timers=[]
for i in xrange(page_count):
	timers.append(timer(user_url+'&page='+str(i+1)))
	
time1=time.time()
for i in xrange(page_count):
	timers[i].setDaemon(True)
	timers[i].start()


for i in xrange(page_count):
	timers[i].join()
time2=time.time()
print time2-time1
