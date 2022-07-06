import os
from sys import exit
import hmac
import secrets
import jwt
from hashlib import pbkdf2_hmac
from base64 import b64encode
from flask import render_template, request, make_response, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/www/epf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

JWT_SECRET = os.getenv('JWT_SECRET')
if not JWT_SECRET:
    print('JWT_SECRET is not set')
    exit()

def hash_passwd(passwd):
    return b64encode(pbkdf2_hmac('sha256', passwd.encode(), b'', 32768)).decode()

def check_passwd(hashed, passwd):
    return hmac.compare_digest(hashed, hash_passwd(passwd))

class Users(db.Model):
    """
    create table users (
      username varchar(255) primary key,
      pepper char(16) not null,
      password varchar(255) not null
    );
    """
    username = db.Column(db.String(255), primary_key=True)
    pepper = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(255), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['username'].strip() == '':
            return render_template('index.html', error='Username is required')
        if request.form['password'].strip() == '':
            return render_template('index.html', error='Password is required')
        
        result = Users.query.filter_by(username=request.form['username']).first()
        if not result:
            return render_template('index.html', error='Username not found')
        if not check_passwd(result.password, request.form['password'] + result.pepper):
            return render_template('index.html', error='Incorrect password')

        payload = {'username': result.username}
        token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
        response = make_response(render_template('dashboard.html', username=result.username))
        response.set_cookie('token', token)
        return response

    else:
        # check if token is valid
        token = request.cookies.get('token')
        if token:
            try:
                payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
                return render_template('dashboard.html', username=payload['username'])
            except jwt.ExpiredSignatureError:
                pass
            except jwt.InvalidTokenError:
                pass
        
        resp = make_response(render_template('index.html'))
        resp.set_cookie("flag-2", value=r"COMPCLUB{p3NgU1N_L0Ve$_c0oK1ez}")
        return resp

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if they are already logged in, redirect to dashboard
    token = request.cookies.get('token')
    if token:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            return render_template('dashboard.html', username=payload['username'])
        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass
    
    if request.method == 'POST':
        if request.form['username'].strip() == '':
            return render_template('register.html', error='Username is required')
        if request.form['password'].strip() == '':
            return render_template('register.html', error='Password is required')
        if len(request.form['password']) < 8:
            return render_template('register.html', error='Password must be at least 8 characters')

        # check if username is taken
        result = Users.query.filter_by(username=request.form['username']).first()
        if result:
            return render_template('register.html', error='Username already taken')

        # create user
        user_pepper = secrets.token_urlsafe(16)
        user = Users(
            username=request.form['username'],
            pepper=user_pepper,
            password=hash_passwd(request.form['password'] + user_pepper)
        )
        db.session.add(user)
        db.session.commit()

        # log them in
        payload = {'username': user.username}
        token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
        response = make_response(render_template('dashboard.html', username=user.username))
        response.set_cookie('token', token)
        return response
    else:
        return render_template('register.html')
            
@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('token', '', expires=0)
    return response

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')
