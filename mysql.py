import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='python',port=3306)
cur=conn.cursor()
cur.execute('select * from weibo')
cur.close()
conn.close()

