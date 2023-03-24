import random
import cgi

# Définition de la fonction de tri à bulle
def bubble_sort(numbers):
    n = len(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

# Génération des nombres aléatoires
numbers = [random.randint(0, 100) for _ in range(10)]

# Copie de la liste avant le tri
unsorted_numbers = numbers.copy()

# Tri des nombres
bubble_sort(numbers)

# Rendu HTML
print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<meta charset='utf-8'>")
print("<title>Tri à bulle</title>")
print("<style>")
print("body { font-family: sans-serif; background-color: #f8f8f8; }")
print("h1 { text-align: center; margin-top: 40px; }")
print("ul { list-style-type: none; padding: 0; margin: 20px auto; width: 300px; }")
print("li { padding: 10px; margin-bottom: 5px; background-color: #fff; border-radius: 5px; box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1); }")
print("</style>")
print("</head>")
print("<body>")
print("<h1>Tri a bulle de 10 nombres aléatoires</h1>")
print("<h2>Liste Non triee:</h2>")
print("<ul>")
for number in unsorted_numbers:
    print(f"<li>{number}</li>")
print("</ul>")
print("<h2>Liste triee :</h2>")
print("<ul>")
for number in numbers:
    print(f"<li>{number}</li>")
print("</ul>")
print("</body>")
print("</html>")
