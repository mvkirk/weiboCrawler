import MySQLdb
class Database:
	conn=''
	def __init__(self):
		self.conn=MySQLdb.connect(host='localhost',user='root',passwd='15062880460ding',db='weibo',port=3306)
		

	def insertUser(dicts):
		uid=dicts['uid']
		containerId=dicts['containerId']
		name=dicts['name']
		gender=dicts['gender']
		description=dicts['description']
		nativePlace=dicts['nativePlace']
		sql='insert into user(uid,containerId,name,gender,description,nativePlace) values(%s,%s,%s,%s,%s,%s)'
		param=(uid,containerId,name,gender,description,nativePlace)
		cursor=self.conn.cursor()
		n=cursor.execute(sql,param)
		print n
		cursor.close()
		self.conn.commit()
	
	def insertRelation(fans,followers):
		sql='insert into relation(fansId,followerId) values(%s,%s)'
		param=[]
		for follower in followers:
			param.append((fans,follower))
		param=tuple(param)
		cursor=self.conn.cursor()
		n = cursor.executemany(sql,param) 
		print n
		cursor.close()
		self.conn.commit()
	
	def close():
		conn.close()

