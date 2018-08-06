"""
    Data analysis
"""
print("~="*20)
print("{:^20}".format("Análise dados de Entrada"))
print("~="*20)

numbersName = ("primeiro", "segundo", "terceiro", "último")
numbers = tuple(int(input(f"Entre com o {numbersName[i]} numeros: ")) for i in range(4))
appearNumber9 = 0
positionNumber3 = 0
pairNumbers = []

for pos, number in enumerate(numbers):
    if number == 9:
        appearNumber9 += 1
    if number == 3 and positionNumber3 <= 0:
        positionNumber3 = pos+1
    if number % 2 == 0:
        pairNumbers.append(number)

if appearNumber9:
    print(f"O número 9 apareceu {appearNumber9} vezes.")
if positionNumber3:
    print(f"O primeiro valor 3 apareceu na posição {positionNumber3}.")
if pairNumbers:
    print(f"Os números pares foram {pairNumbers}.")

print("~="*20)
