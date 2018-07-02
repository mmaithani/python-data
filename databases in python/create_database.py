# Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors

#Ans.1-

import pymysql
db=pymysql.connect("localhost","root","mamipapasumit81","acad_assign")
cursor=db.cursor()
cursor.execute("create table book(userid int,titleid int,location char(25),genre int)")
cursor.execute("create table title(titleid int,title int,publisherid char(20),publisher_year int)")
db.close()


