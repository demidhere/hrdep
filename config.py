from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'Demid4here.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'Demid4here'
app.config['MYSQL_DATABASE_PASSWORD'] = 'QV8eH@3cH2bsjn@'
app.config['MYSQL_DATABASE_DB'] = 'Demid4here$hrdep_db'

mysql = MySQL()
mysql.init_app(app)