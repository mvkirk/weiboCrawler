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
	try:#parse error,omit it.
		followers=follower.getFollowers(dicts['containerId'])
	except:
		return
	for it in followers:
		if not queue.full():
			queue.put(it)	
	db.insertRelation(uid,followers)
	logging.info(str(uid)+'\t'+dicts['name']+" has been recorded.")

if __name__=='__main__':
	startUid='2002575703'
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
		except:
			print 'lost connection'
			db=database.Database()
	db.close()
