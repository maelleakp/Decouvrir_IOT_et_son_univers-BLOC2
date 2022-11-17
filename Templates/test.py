import pymysql.cursors
from matplotlib.figure import Figure

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='bloc2',
                             charset='utf8mb4',
                             port = 8889,
                             cursorclass=pymysql.cursors.DictCursor)

# SQL
cursor = connection.cursor()
cursor.execute("Select TEMP_R, ID_R from Releve where NUM_C = '62182233'")
result = cursor.fetchall()
TEMP = []
ID = []
for donnees in result:
    TEMP.append(donnees['TEMP_R'])
    ID.append(donnees['ID_R'])

print("Température = ", TEMP)
print("ID = ", ID)

# visualisation du graphique
fig = Figure()
ax1 = fig.subplots(1, 1)
ax1.plot(ID, TEMP)
fig.savefig("test.png", format="png")
