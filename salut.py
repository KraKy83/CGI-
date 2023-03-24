#!/usr/bin/env python3
import cgi
import datetime

# Récupération des données du formulaire
form = cgi.FieldStorage()
nom = form.getvalue("nom")
civilite = form.getvalue("civilite")

# Détermination de l'heure actuelle
maintenant = datetime.datetime.now()
heure = maintenant.hour

# Génération de la phrase de salutation en fonction de l'heure
if heure >= 18:
    salutation = "Bonsoir"
else:
    salutation = "Bonjour"

# Personnalisation de la salutation avec le nom
if nom:
    salutation += " " + civilite + " " + nom
else:
    salutation += " " + civilite

# Affichage de la réponse
print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<meta charset='utf-8'>")
print("<title>Réponse à votre salutation</title>")
print("</head>")
print("<body>")
print("<h1>{}</h1>".format(salutation))
print("<p>{}, il est {}h{}</p>".format(salutation, maintenant.hour, maintenant.minute))
print("</body>")
print("</html>")
