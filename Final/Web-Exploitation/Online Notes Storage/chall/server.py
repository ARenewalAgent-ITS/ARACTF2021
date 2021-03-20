
from datetime import datetime

import jwt as jwt_imp
import base64,json,hashlib ,os
from encryption import encrypt,decrypt
from flask import Flask, jsonify, request, current_app, render_template , make_response , redirect, render_template_string
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt
)
from flask_mysqldb import MySQL
from flask_jwt_simple.config import config
from config_db import *
import MySQLdb.cursors

key = "" 

def decode_jwt(encoded_token):
    try:
        tmp = encoded_token.split(".")[0]
        algorithm = json.loads(base64.b64decode(tmp+'='*(4-len(tmp)%4)))['alg']
        if(algorithm!='HS256'):
            return 'error'
        secret = config.decode_key
        audience = config.audience
        return jwt_imp.decode(encoded_token, secret, algorithms=[algorithm], audience=audience,verify=False)
    except Exception as e:
        return 'error'

app = Flask(__name__)
app.config['MYSQL_HOST'] = server_db
app.config['MYSQL_USER'] = username_db
app.config['MYSQL_PASSWORD'] = password_db
app.config['MYSQL_DB'] = name_db
mysql = MySQL(app)

app.config['JWT_SECRET_KEY'] = ''
jwt = JWTManager(app)


@jwt.jwt_data_loader
def add_claims_to_access_token(identity):
    now = datetime.utcnow()
    return {
        'exp': now + current_app.config['JWT_EXPIRES'],
        'iat': now,
        'nbf': now,
        'sub': identity[0],
        'roles': identity[1]
    }


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            ret =  create_jwt([hashlib.md5((username+password).encode()).hexdigest(),account['roles']])
        else:
            return jsonify(msg="Username or Password Incorrect!"), 403
        response = make_response(redirect('/protected'))
        response.set_cookie('token', ret)
        return response
    else:
        if(request.cookies.get('token')):
            return make_response(redirect('/protected'))
        return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        roles = "not_member"
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(username, password, roles) VALUES (%s, %s, %s)", (username, password, roles))
            mysql.connection.commit()
            cur.close()
        except Exception as e:
            return jsonify(msg="Error!"), 500
        ret = create_jwt([hashlib.md5((username+password).encode()).hexdigest(),roles])
        response = make_response(redirect('/protected'))
        response.set_cookie('token', ret)
        return response
    else:
        return render_template('register.html')

@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        response = make_response(redirect('/'))
        response.delete_cookie('token')
        return response

@app.route('/view_notes/<id_notes>', methods=['POST','GET'])
def view_notes(id_notes):
    #todo

@app.route('/protected', methods=['GET','POST'])
def protected():
    if request.method == 'POST':
        jwt_data=decode_jwt(request.cookies.get('token'))
        if jwt_data['roles'] != 'member':
            return jsonify(msg="Permission denied, You are not a member"), 403
        if jwt_data=='error':
            return jsonify(msg="Something Wrong!"), 403
        uploaded_file = request.files['file']
        title = request.form['title']
        name=uploaded_file.filename
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('./static/uploads/',name))
            f=open(os.path.join('./static/uploads/',name),"rb")
            tmp = f.read()
            if(b'\x9f\x63' in tmp):
                tmp = tmp.replace(b'\x9f\x63',b'\xdb\x27')
            enc = encrypt(key,tmp)
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO storage(title, notes, id) VALUES (%s, %s, %s)", (title, enc, jwt_data['sub']))
            mysql.connection.commit()
            cur.close()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * from storage where (id=%s) " ,(jwt_data['sub'],))
        result = cur.fetchall()
        return render_template('protected.html',result=result)
    else:
        jwt_data=decode_jwt(request.cookies.get('token'))
        if jwt_data=='error':
            return jsonify(msg="Something Wrong!"), 403
        if jwt_data['roles'] != 'member':
            return jsonify(msg="Permission denied, You are not a member"), 403
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * from storage where (id=%s) " ,(jwt_data['sub'],))
        result = cur.fetchall()
        if result:
            return render_template('protected.html',result=result)
        return render_template('protected.html')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    import sys,logging
    app.logger.disabled = True
    log = logging.getLogger('werkzeug')
    log.disabled = True
    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None
    app.run(debug=True,host='0.0.0.0',port=8010)