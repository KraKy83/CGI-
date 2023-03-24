#!/usr/bin/env python3
import cgi

# Définition de la fonction de tri par sélection
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

# Récupération des nombres saisis par l'utilisateur
form = cgi.FieldStorage()
numbers_str = form.getfirst("numbers")
if numbers_str:
    numbers = [int(x) for x in numbers_str.split(",")]
else:
    # Génération des nombres aléatoires si aucun nombre n'a été saisi
    import random
    numbers = [random.randint(0, 100) for _ in range(10)]

# Tri des nombres
selection_sort(numbers)

# Rendu HTML
print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<meta charset='utf-8'>")
print("<title>Tri par selection</title>")
print("<style>")
print("body { font-family: sans-serif; background-color: #f8f8f8; }")
print("h1 { text-align: center; margin-top: 40px; }")
print("ul { list-style-type: none; padding: 0; margin: 20px auto; width: 300px; }")
print("li { padding: 10px; margin-bottom: 5px; background-color: #fff; border-radius: 5px; box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1); }")
print("</style>")
print("</head>")
print("<body>")
print("<h1>Tri par sélection de 10 nombres aléatoires</h1>")
print("<form method='post'>")
print("<label for='numbers'>Liste de nombres (separes par des virgules) :</label>")
print("<input type='text' name='numbers' id='numbers'>")
print("<input type='submit' value='Trier'>")
print("</form>")
print("<ul>")
for number in numbers:
    print(f"<li>{number}</li>")
print("</ul>")
if numbers_str:
    print("<h1>Liste triée</h1>")
    print("<ul>")
    for number in numbers:
        print(f"<li>{number}</li>")
    print("</ul>")
print("</body>")
print("</html>")
