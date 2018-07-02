# Q.3- Update any values in any of the tables. Print the original and updated values.
#a.3-


import pymysql as py

db=py.connect("localhost","root","*************8","library")
cursor=db.cursor()
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
cursor.execute("update book set genre='philosophy' where book_id=001")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()