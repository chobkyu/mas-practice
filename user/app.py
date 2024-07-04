from flask import Flask, jsonify, session, request, redirect
import json
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/api/user',methods=["POST"])
def login():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DATABASE', 'test_db')
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    
    print(result)
    session['username'] = request.form["username"]
    return redirect("/w/login", code=302)

@app.route("/api/user",methods=["GET"])
def get():
    if "username" in session:
        print(session["username"])
        return ("session found:"+session["username"])
    else:
        return ("Session not found: ")
    

@app.route("/api/user/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect('/w/login',code=302)


@app.route("/api/user/test",methods=["GET"])
def test():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DATABASE', 'test_db')
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=9002,
        debug=True
    )
