def convertir(chaine):
    CP1 = "62182233"
    CP2 = "06182660"
    CP3 = "06190484"
    id_capteur = [CP1, CP2, CP3]

    for capteur in id_capteur :
        #print("capteur", capteur)
        if capteur in chaine :
            #print(capteur)
            if capteur == "62182233" :
                # afficher l'humidité
                position_hum = chaine.find(capteur) + 18
                valeur_hum = chaine[position_hum : position_hum + 2]
                humidité = int(valeur_hum, 16)
                #print("L'humidité de " + capteur + " est de " + str(humidité) + "%.")
            else :
                humidité = 0

            # afficher la température
            position_temp = chaine.find(capteur) + 14
            valeur_temp = chaine[position_temp : position_temp+4]
            if valeur_temp[0:1] == '4':
                température = (int(valeur_temp[1:4], 16) / 10) * -1
            else:
                température = int(valeur_temp[1:4], 16) / 10
            #print("La température de " + capteur + " est " + str(round(température, 1)) + "°C.")

            # afficher le niveau de batterie
            position_bat = chaine.find(capteur)+10
            valeur_bat = chaine[position_bat :position_bat+4]
            batterie = (int(valeur_bat[1:4], 16) / 1000)
            #print("La batterie de "  + capteur + " est " + str(round(batterie, 3)) + "V.")

            # afficher le signal RSSI
            position_sig = chaine.find(capteur)+20
            valeur_sig = chaine[position_sig : position_sig+2]
            signal = (int(valeur_sig[0:2], 16)) * -1
            #print("Le signal RSSI de " + capteur + " est -" + str(signal) + "dBm.")
        else :
            return None

        sauvegarde(capteur, température, humidité, batterie, signal)


def sauvegarde(capteur, température, humidité, batterie, signal):
    import pymysql.cursors
    con = pymysql.connect(host='localhost', user="root", password="root", database='bloc2', port = 8889)
    cur = con.cursor()
    mareq = "INSERT INTO `Releve`(`NUM_C`, `TEMP_R`, `HUM_R`, `BATT_R`, `RSSI_R`) VALUES (" \
            "%s, %s, %s, %s, %s" + ")"
    print(capteur, température, humidité, batterie, signal)
    cur.execute(mareq, (capteur, température, humidité, batterie, signal))
    rep = cur.rowcount
    con.commit()
    con.close()
    return rep