import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase')
)

class Users:
    def signup(self,username,password):
        db.ping(reconnect=True)
        dbcursor=db.cursor(dictionary=True,buffered=True)
        querry = 'insert into user_info(users,password) values(%s,%s)'
        dbcursor.execute(querry,(username,password,))
        db.commit()
        dbcursor.close()
        db.close()
    def login(self,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select id,users,password from user_info where users=%s'
        dbcursor.execute(querry,(username,))
        result=dbcursor.fetchall()
        dbcursor.close()
        db.close()
        return result
    def change_pwd(self,password,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='update user_info set password=%s where users=%s'
        dbcursor.execute(querry,(password,username,))
        db.commit()
        db.close()
        dbcursor.close()cd\



class Verify(Users):
    def check_username(self,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select users from user_info where users=%s'
        dbcursor.execute(querry,(username,))
        result=dbcursor.fetchone()
        dbcursor.close()
        return result
    def user_info_querry(self):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select * from user_info'
        dbcursor.execute(querry)
        result=dbcursor.fetchall()
        dbcursor.close()
        return result


