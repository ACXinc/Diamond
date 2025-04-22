
from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # replace with a stronger secret in production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add authentication logic here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/create', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form.get('phone', '')
        # Save account logic here
        return redirect(url_for('login'))
    return render_template('create.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin_panel():
    return render_template('admin.html')

@app.route('/blocked', methods=['GET', 'POST'])
def blocked_account():
    if request.method == 'POST':
        holder = request.form['holder']
        amount = request.form['amount']
        # Save blocked account logic here
        return redirect(url_for('home'))
    return render_template('blocked.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

