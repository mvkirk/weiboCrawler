#encoding=utf-8
import MySQLdb
class Database:
	conn=''
	def __init__(self):
		self.conn=MySQLdb.connect(host='localhost',user='root',passwd='15062880460ding',db='weibo',port=3306,charset='utf8')
		
	def insertUser(self,dicts):
		uid=dicts['uid']
		containerId=dicts['containerId']
		name=dicts['name']
		gender=dicts['gender']
		description=dicts['description']
		nativePlace=dicts['nativePlace']
		sql='insert into user(uid,containerId,name,gender,description,nativePlace) values(%s,%s,%s,%s,%s,%s)'
		param=[uid,containerId,name,gender,description,nativePlace]
		cursor=self.conn.cursor()
		n=cursor.execute(sql,param)
		cursor.close()
		self.conn.commit()
	
	def insertRelation(self,fans,followers):
		sql='insert into relation(fansId,followerId) values(%s,%s)'
		param=[]
		for follower in followers:
			param.append((fans,follower))
		cursor=self.conn.cursor()
		n = cursor.executemany(sql,param) 
		cursor.close()
		self.conn.commit()
	
	def findUser(self,uid):
		sql='select uid from user where uid=%s'
		param=[uid]
		cursor=self.conn.cursor()
		n = cursor.execute(sql,param) 
		cursor.close()
		self.conn.commit()
		return n!=0

	def close(self):
		self.conn.close()
if __name__=='__main__':
	pass
