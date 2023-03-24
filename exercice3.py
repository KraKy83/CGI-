
import cgi
import mysql.connector

# Paramètres de connexion à la base de données
host = "10.10.10.41"
user = "etudiant"
password = "Promo2024"
database = "test"

# Entête HTTP
print("Content-Type: text/html")
print()

# Récupération des données du formulaire
form = cgi.FieldStorage()
dep_num = form.getvalue("dep_num")

# Si aucun numéro de département n'a été soumis, afficher le formulaire
if dep_num is None:
    print("<h1>Recherche de département</h1>")
    print('<form method="get">')
    print('<label for="dep_num">Numéro de département :</label>')
    print('<input type="text" name="dep_num" id="dep_num">')
    print('<input type="submit" value="Rechercher">')
    print('</form>')
else:
    # Connexion à la base de données
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        print("Connexion réussie à la base de données")
    except mysql.connector.Error as e:
        print("Erreur lors de la connexion à la base de données :", e)

    # Récupération du département correspondant
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT departement_code, departement_nom FROM departement WHERE departement_code = %s", (dep_num,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                print(f"Le département correspondant au numéro {dep_num} est : {rows[0][1]} ({rows[0][0]})")
            else:
                print(f"Aucun département ne correspond au numéro {dep_num}")
    except mysql.connector.Error as e:
        print("Erreur lors de l'exécution de la requête SQL :", e)

    # Fermeture de la connexion à la base de données
    conn.close()
