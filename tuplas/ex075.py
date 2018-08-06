"""
    Data analysis
"""
print("~="*20)
print("{:^20}".format("Análise dados de Entrada"))
print("~="*20)

numbersName = ("primeiro", "segundo", "terceiro", "último")
numbers = tuple(int(input(f"Entre com o {numbersName[i]} numeros: ")) for i in range(4))
pairNumbers = []

for number in numbers:
    if number % 2 == 0:
        pairNumbers.append(number)

if numbers.count(9):
    print(f"O número 9 apareceu {numbers.count(9)} vezes.")
if 3 in numbers:
    print(f"O primeiro valor 3 apareceu na posição {numbers.index(3)}.")
if pairNumbers:
    print(f"Os números pares foram {pairNumbers}.")

print("~="*20)
