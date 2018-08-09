"""
    Game of the Mega Sena
"""
from random import sample

print("~="*20)
print(f"{'Jog da Mega Sena':^40}")
print("~="*20)

numberGames = int(input("Quantos jogos você quer que eu sorteie? "))

print("~="*4, f" Sorteando {numberGames} Jogos ", "~="*4)

for i in range(0, numberGames):
    game = sorted(sample(range(1, 61), 6))
    print(f"Jogo {i+1}: {game}")

print("~="*5, "< Boa Sorte! >", "~="*5)
print("~="*20)
