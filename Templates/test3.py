
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
cursor.execute("Select TEMP_R, ID_R from Releve where NUM_C = '06190484'")
result = cursor.fetchall()
TEMP = []
ID = []
for donnees in result:
    TEMP.append(donnees['TEMP_R'])
    ID.append(donnees['ID_R'])

print("Température = ", TEMP)
print("ID = ", ID)

# Visulizing Data using Matplotlib
fig = Figure()
ax1 = fig.subplots(1, 1)
ax1.plot(ID, TEMP)
fig.savefig("test3.png", format="png")

# plt.plot(ID, TEMP)
# plt.ylim(0, 30)
# plt.ylabel("Température")
# plt.title("Graphe 1")
# plt.show()
# fig.savefig("test.png", format="png")