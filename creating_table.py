import mysql.connector as ms
import time

tim= time.localtime()

mydb = ms.connect(host="localhost", user="mimir", passwd="Mrin@l123")

month={'1':31,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}

cursorObject = mydb.cursor()
a="name varchar(100),rollno varchar(32)"
dat=month[f'{tim.tm_mon}']
for i in range(1,dat):
    a+=f",`{i}` varchar(1)"


cursorObject.execute("use attendance;")
cursorObject.execute(f"create table `{tim.tm_mon}`({a});")