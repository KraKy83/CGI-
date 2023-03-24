#!/usr/bin/env python3
import cgi

def feet_to_meter(feet):
    meter = feet * 0.3048
    return round(meter, 2)

def meter_to_feet(meter):
    feet = meter / 0.3048
    return round(feet, 2)

form = cgi.FieldStorage()

if "altitude" in form and "unite" in form:
    altitude = float(form.getvalue("altitude"))
    unite = form.getvalue("unite")

    if unite == "ft":
        altitude_converted = feet_to_meter(altitude)
        unite_converted = "m"
    elif unite == "m":
        altitude_converted = meter_to_feet(altitude)
        unite_converted = "ft"

    if altitude_converted >= 15500 or altitude >= 50800:
        image_path = "image/business_jet.png"
    elif (altitude_converted >= 10000 and altitude_converted <= 13000) or (altitude >= 32000 and altitude <= 42000):
        image_path = "image/long-courrier.png"
    elif altitude_converted >= 7000 and altitude_converted <= 9999 or altitude >= 23000 and altitude <= 31999:
        image_path = "image/moyen-courrier.png"
    elif altitude_converted >= 5100 and altitude_converted <= 6999 or altitude >= 17000 and altitude <= 22999:
        image_path = "image/regional.png"
    elif altitude_converted >= 1000 and altitude_converted <= 4999 or altitude >= 3300 and altitude <= 16999:
        image_path = "image/tourisme.png"


    message = "{} {} equivaut a {} {}.".format(altitude, unite, altitude_converted, unite_converted)
    image_html = "<img src='{}'>".format(image_path)
else:
    message = "Veuillez entrer une altitude et une unité de mesure."
    image_html = ""

print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<meta charset='utf-8'>")
print("<title>Résultat de la conversion d'altitude</title>")
print("<link rel='stylesheet' href='css/style.css'>")
print("</head>")
print("<body>")
print("<h1>Convertisseur d'altitude</h1>")
print("<p>{}</p>".format(message))
print(image_html)
print("<a href='conversion.html'>Retour</a>")
print("</body>")
print("</html>")
