# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", data = data)

@app.route("/capteur1")
def cp1():
    return render_template("capteur1.html", data = data)
@app.route("/histocp1")
def histocp1():
    return render_template("histocp1.html")
@app.route("/capteur2")
def cp2():
    return render_template("capteur2.html", data = data)
@app.route("/histocp2")
def histocp2():
    return render_template("histocp2.html")

@app.route("/capteur3")
def cp3():
    return render_template("capteur3.html", data = data)
@app.route("/histocp3")
def histocp3():
    return render_template("histocp3.html")

import pymysql.cursors
# connection la base de données.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='bloc2',
                             charset='utf8mb4',
                             port = 8889,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # requête SQL
        sql = "Select * from Releve where DATEHEURE_R = (SELECT MAX(DATEHEURE_R) as 'DERNIER-DATE' from Releve)"

        # exécuter la requête
        cursor.execute(sql)
        data = cursor.fetchall()

finally:
    # fermer la connexion
    connection.close()

if __name__ == "__main__":
    app.run(debug=True, port=8889)