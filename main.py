import requests
import script

# Récupère les données issu de l'API
response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=1")
dico = response.json()

# Envoie la chaine récupérée dans la fonction convertir
script.convertir(dico[0][1])