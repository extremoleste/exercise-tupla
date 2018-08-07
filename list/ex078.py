"""
    Max & Min value by position
"""
print("~="*20)
print(f"{'Maior e Menor valor e suas Posições':^40}")
print("~="*20)

maxNumbers = ""
minNumbers = ""
numbers = list(int(input(f"Valor da posições {i}: ")) for i in range(0,5))

print("-"*40)
print(f"Você digitou os valores {numbers}")

for pos, number in enumerate(numbers):
    if max(numbers) == number:
        maxNumbers += f"{pos}... "
    if min(numbers) == number:
        minNumbers += f"{pos}... "

print(f"O maior valor é {max(numbers)} e está em: {maxNumbers}")
print(f"O menor valor é {min(numbers)} e está em: {minNumbers}")
print("~="*20)
