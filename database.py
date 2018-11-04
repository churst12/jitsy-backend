import os
import psycopg2


URI = 'postgres://rtenrdgxkeegwf:fbd0820662a2bbdfb1352725a41f250ab8ed1b2afa3d728bdf584ce0411eabc3@ec2-184-73-169-151.compute-1.amazonaws.com:5432/dfv0kjpehdd0bn'


conn = psycopg2.connect(URI, sslmode='require')

cur = conn.cursor()
cur.execute('select * from information_schema.tables')
print(cur.fetchone())