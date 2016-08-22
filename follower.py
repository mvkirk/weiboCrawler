#encoding:utf-8
import urllib2,cookielib,urllib,json,sys,time,re
from bs4 import BeautifulSoup 

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('User-agent','Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')]
urllib2.install_opener(opener)

user_url="http://m.weibo.cn/u/5587464347"


request=urllib2.urlopen(user_url)
html=request.read()
html=html.replace('\n',' ')

f=open('response.txt','w')
soup=BeautifulSoup(html,"lxml").prettify('utf-8') 
f.write(soup)
config=re.findall(r'window.\$config=(.*?);',html)[0]
render=re.findall(r'window.\$render_data =(.*?);',html)[0]
config=config.replace(' ','')
config=config.replace('\'','\"')
render=render.replace(' ','')
render=render.replace('\'','\"')
config_decoded=json.loads(config)
render_decoded=json.loads(render)

f.write(json.dumps(config_decoded,indent=4))
f.write(json.dumps(render_decoded,indent=4))