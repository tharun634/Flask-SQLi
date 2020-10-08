from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flasktut'

mysql = MySQL(app)


@app.route('/login/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        
        user = details['user']
        password = details['pass']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE user = %(username)s AND pass = %(password)s", {'username': user,'password': password})
        
        account = cur.fetchone()
        if account:
            return 'Logged in successfully'
        else:
            # Account doesnt exist or username/password incorrect
            return 'Log in failed, Wrong Credentials'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()