# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", data = data)

import pymysql.cursors
# Connectez- vous à la base de données.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='bloc2',
                             charset='utf8mb4',
                             port = 8889,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # SQL
        sql = "Select * from Releve where DATEHEURE_R = (SELECT MAX(DATEHEURE_R) as 'DERNIER-DATE' from Releve)"
        # Exécutez la requête (Execute Query).
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
finally:
    # Closez la connexion (Close connection).
    connection.close()

if __name__ == "__main__":
    app.run(debug=True, port=8889)