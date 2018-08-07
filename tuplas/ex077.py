"""
    Found Vowels
"""
print("~="*20)
print(f"{'Vogais Encontradas':^40}")
print("~="*20)

words = (
    "APRENDER",
    "PROGRAMAR",
    "LINGUAGEM",
    "PYTHON",
    "CURSO",
    "GRATIS",
    "ESTUDAR",
    "PRATICAR",
    "TRABALHAR",
    "MERCADO",
    "PROGRAMADOR",
    "FUTURO"
)
vowels = ("a", "e", "i", "o", "u")

for word in words:
    foundVowels = []
    for letter in word:
        if letter.lower() in vowels:
            foundVowels.append(letter)
    found = " ".join(foundVowels)
    print(f"Na palavra {word} é possível entrocar as Vogais: {found}")

print("~="*20)
