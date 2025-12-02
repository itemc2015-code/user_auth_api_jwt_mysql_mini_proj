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
    def signup(username,password):
        querry = 'insert into user_info(users,password) values(%s,%s)'

