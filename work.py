import follower,database,sys,Queue,logging,time

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='log.txt',
                filemode='w+')

db=database.Database()
queue=Queue.Queue(1000000)

def process():
	uid=queue.get()
	if db.findUser(uid):
		return
	try:
		dicts=follower.getUser(uid)
	except:
		return
	db.insertUser(dicts)
	try:
		followers=follower.getFollowers(dicts['containerId'])
	except:
		return
	for it in followers:
		if not queue.full():
			queue.put(it)	
	db.insertRelation(uid,followers)
	logging.info(str(uid)+'\t'+dicts['name']+" has been recorded.")

if __name__=='__main__':
	startUid='1667553532'
	if db.findUser(startUid):
		dicts=follower.getUser(startUid)	
		followers=follower.getFollowers(dicts['containerId'])
	        for it in followers:
        	        if not queue.full():
	                        queue.put(it)
	else:
		queue.put(startUid)
	cnt=0
	while not queue.empty():
		process()
		cnt+=1
		if cnt%100==0:
			cnt=0
			time.sleep(1800)
	db.close()
