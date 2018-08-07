"""
    Data Analysis
"""
print("~="*20)
print(f"{'Análise de Dados':^40}")
print("~="*20)

numbers = []
pairs = []
odd = []

while True:
    numbers.append(int(input("Digite um valor: ")))
    print("-"*40)
    continuos = str(input("Deseja continuar [s/n]: ")).lower()
    while continuos not in "sn":
        continuos = str(input("Deseja continuar [s/n]: ")).lower()
    print("-"*40)
    if continuos in "n":
        break

for number in numbers:
    if number % 2 == 0:
        pairs.append(number)
    else:
        odd.append(number)

print(f"Lista dos números digitados: {numbers}")
print(f"Lista dos números pares digitados: {pairs}.")
print(f"Lista dos números ímpares digitados: {odd}.")
print("~="*20)
