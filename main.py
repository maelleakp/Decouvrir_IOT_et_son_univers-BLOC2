import requests
import script

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=1")

dico = response.json()
rep = script.convertir(dico[0][1])



