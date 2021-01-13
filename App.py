from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf import CsrfProtect
#from flask_bootstrap import Bootstrap
from config import devConfig

app = Flask(__name__)

# Settings
app.config.from_object(devConfig)

# Token
csrf = CsrfProtect()

# Bootstrap 3
#Bootstrap(app)

# MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts ORDER BY fullname ASC')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)


@app.route('/create', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts(fullname,phone,email) VALUES (%s,%s,%s)',(name,phone,email))
        mysql.connection.commit()
        flash('contact added successfully')
        return redirect(url_for('index'))


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s',(id))
    data = cur.fetchone()
    return render_template('edit.html', contact = data)


@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute('''UPDATE contacts 
        SET fullname = %s,phone = %s,email = %s
        WHERE id = %s''',(name,phone,email,id))
    mysql.connection.commit()
    flash('contact updated successfully')
    return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('contact removed successfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    csrf.init_app(app)

    app.run(port=3000)
