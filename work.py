import follower,database,sys,Queue,logging,time

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='userGet.log',
                filemode='a')

db=database.Database()
queue=Queue.Queue(1000000)

def process():
	uid=queue.get()
	if db.findUser(uid):
		return
	try:#parse error,then omit it.
		dicts=follower.getUser(uid)
	except:
		return
	db.insertUser(dicts)
	logging.info(str(uid)+'\t'+dicts['name']+" will be recorded.")
	print 'inserUser done'
	try:
		data=follower.getStarredUsers(dicts['containerId'])
	except:
		return
	try:
		db.insertStar(uid,data)
	except:
		pass
	print 'insertStar done'
	try:#parse error,omit it.
		followers=follower.getFollowers(dicts['containerId'])
	except:
		return
	for it in followers:
		if not queue.full():
			queue.put(it)	
	db.insertRelation(uid,followers)
	print 'insertRelation done'
	logging.info(str(uid)+'\t'+dicts['name']+" has been recorded.")

if __name__=='__main__':
	#startUid='5320278224' me
	startUid='5320278224'
	if db.findUser(startUid):
		dicts=follower.getUser(startUid)	
		followers=follower.getFollowers(dicts['containerId'])
	        for it in followers:
        	        if not queue.full():
	                        queue.put(it)
	else:
		queue.put(startUid)
	while not queue.empty():
		try:
			process()
		except Exception,e:
			print 'lost connection'
			print e
			db=database.Database()
	db.close()
