#encoding:utf-8
from bs4 import BeautifulSoup 
import urllib2,cookielib,urllib,json,sys,time,re,threading,random
from  opener import Opener

def queryFollower(url):
	urllib2.install_opener(Opener().getOpener())
	while True:
		try:
			request=urllib2.urlopen(url)
			break
		except:
			pass
	html=request.read()
	html=html.replace('\n',' ')
	data=json.loads(html)
	return data



class timer(threading.Thread):
	url=""
	res=[]
	def __init__(self,url,res):
		threading.Thread.__init__(self)
		self.url=url
		self.res=res
	
	def run(self):	
		data=queryFollower(self.url)
		for j in xrange(10):
			try:
				user=data['cards'][0]['card_group'][j]
				uid=user['user']['id']
				self.res.append(uid)
			except:
				pass

def getFollowers(containerId):
	user_url="http://m.weibo.cn/page/json?containerid="+containerId+"_-_FOLLOWERS"
	data=queryFollower(user_url)
	formated=json.dumps(data,indent=4)
	f=open('response.txt','w')
	f.write(formated.decode('unicode-escape').encode('utf-8'))
	count=data['count']
	page_count=(count-1)/10+1
	timers=[]
	res=[]
	for i in xrange(page_count):
		timers.append(timer(user_url+'&page='+str(i+1),res))
	for i in xrange(page_count):
		timers[i].setDaemon(True)
		timers[i].start()
	for i in xrange(page_count):
		timers[i].join()
	return res


def getUser(uid):
	urllib2.install_opener(Opener().getOpener())
	user_url="http://m.weibo.cn/u/"+uid
	request=urllib2.urlopen(user_url)
	html=request.read()
	html=html.replace('\n',' ')
	config=re.findall(r'window.\$config=(.*?);',html)[0]
	render=re.findall(r'window.\$render_data =(.*?);',html)[0]
	config=config.replace(' ','')
	config=config.replace('\'','\"')
	render=render.replace(' ','')
	render=render.replace('\'','\"')
	config_decoded=json.loads(config)
	render_decoded=json.loads(render)

	containerId= render_decoded['common']['containerid']
	Id=render_decoded['stage']['page'][1]['id']
	description=render_decoded['stage']['page'][1]['description']
	nativePlace=render_decoded['stage']['page'][1]['nativePlace']
	name=render_decoded['stage']['page'][1]['name']
	gender=render_decoded['stage']['page'][1]['ta']
	dicts={}
	dicts['uid']=Id
	dicts['containerId']=containerId
	dicts['description']=description
	dicts['nativePlace']=nativePlace
	dicts['name']=name
	dicts['gender']=gender
	return dicts
	
if __name__=='__main__':
	uid='1660141095'
	containerId='1005051660141095'
	dicts=getUser(uid)
	res=getFollowers(dicts['containerId'])
	print res
	print len(res)


