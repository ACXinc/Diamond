
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {}
admins = {'admin': 'Admin123'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/home')
        elif username in admins and admins[username] == password:
            session['admin'] = username
            return redirect('/admin')
        else:
            return "Invalid credentials!"
    return render_template('login.html')

@app.route('/create', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect('/login')
    return render_template('create_account.html')

@app.route('/home')
def user_home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('home.html')

@app.route('/admin')
def admin_panel():
    if 'admin' not in session:
        return redirect('/login')
    return render_template('admin_panel.html')

@app.route('/blocked')
def blocked_account():
    return "Blocked account feature is under construction."

if __name__ == '__main__':
    app.run(debug=True)
