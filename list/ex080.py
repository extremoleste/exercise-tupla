"""
    Sort numbers in da entry
"""
print("~="*20)
print(f"{'Ordena números na entrada de dados':^40}")
print("~="*20)

numbers = []

for i in range(0, 5):
    number  = int(input("Digite um valor: "))
    if len(numbers) == 0 or max(numbers) < number:
        numbers.append(number)
        print("\033[0:32mAdicionado ao final da lista!\033[m")
    elif min(numbers) > number:
        numbers.insert(0, number)
        print("\033[0:32mAdicionado na posição 0!\033[m")
    elif number > numbers[0] and number < numbers[1]:
        numbers.insert(1, number)
        print("\033[0:32mAdicionado na posição 1!\033[m")
    else:
        numbers.insert(2, number)
        print("\033[0:32mAdicionado na posição 2!\033[m")

print(f"Os valores digitados estão em ordem: {numbers}.")
print("~="*20)
