"""
    Data Analysis
"""
print("~="*20)
print(f"{'Análise de Dados':^40}")
print("~="*20)

numbers = []

while True:
    number = int(input("Digite um valor: "))
    numbers.append(number)
    print("-"*40)
    continuos = str(input("Deseja continuar [s/n]: ")).lower()
    print("-"*40)
    if continuos in "n":
        break
reverseNumbers = sorted(numbers, reverse=True)
print(f"Total de números digitados: {len(numbers)}.")
print(f"Valores digitados na ordem decrescente: {reverseNumbers}.")
if 5 in numbers:
    print(f"O valor 5 foi encontrado primeiramente na posição: {reverseNumbers.index(5)+1}")
else:
    print("O valor 5 não foi digitado!")
print("~="*20)
