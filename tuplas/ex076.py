"""
    Price list
"""
print("~="*20)
print(f"{'Listagem de Preços':^40}")
print("~="*20)

priceList = (
    "Lápis", 1.75,
    "Borracha", 2,
    "Caderno", 12.9,
    "Estojo", 25,
    "Transferiodor", 4.2,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canecas", 22.3,
    "Livro", 34.9
)

for item in priceList:
    if isinstance(item, str): print(f"{item:.<30}", end="")
    else: print(f"R$ {item:>7.2f}")
print("~="*20)
