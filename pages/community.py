
from flask import jsonify, render_template, request, Response

from functions import app
from sqlalchemy import text
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

@app.route('/community', methods=['GET'])
def community():
    sql = text('SELECT * FROM user ORDER BY signup_date DESC LIMIT 5')
    result = db.engine.execute(sql)
    userList = []
    for row in result:
        u = []
        u.append(row[3])
        u.append(row[7])
        u.append(row[11])
        userList.append(u)
    return render_template("community.html", userList=userList)