import socket
import sqlite3 as sq


server=socket.socket(family=socket.AF_INET , type=socket.SOCK_STREAM) 
server.bind(("26.88.178.51",2000))

server.listen(4)


with sq.connect("mySQL1.db",timeout=30) as con:
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS USERS(
       user_id INTEGER PRIMARY KEY,
        name TEXT,
        family TEXT,
       mail TEXT,
        password TEXT    
    )         
    """)
   

while True:
    users=["","","",""]
    user,adres= server.accept()
    for i in range(0,4):
         users[i]=user.recv(1024)
         print(users[0].decode("utf-8"))
    name=str(users[0].decode("utf-8"))
    family=str(users[1].decode("utf-8"))
    mail=str(users[2].decode("utf-8"))
    password=str(users[3].decode("utf-8"))
    user.close()
    print(name,family,mail,password)
    print(users)
    cur.execute("""INSERT INTO USERS (name,family,mail,password)VALUES(?,?,?,?)""",(name,family,mail,password))
    con.commit()
    print("connect")

  
