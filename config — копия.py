from flask import Flask
from flask.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd02167ae514666ce3f204b298b550c7dfbaf3e64'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'university_db'

mysql = MySQL()
mysql.init_app(app)
