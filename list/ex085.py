"""
    List of odd and even numbers in ascending order.
"""
print("~="*20)
print(f"{'Lista de pares e ímpares em ordem':^40}")
print("~="*20)

numbers = list()
pairs = list()
odd = list()

for i in range(0, 7):
    number = int(input("Digite um valor inteiro: "))
    if(number % 2 == 0):
        pairs.append(number)
    else:
        odd.append(number)

numbers.append(sorted(pairs[:]))
numbers.append(sorted(odd[:]))

print(f"Listas originais: {pairs} e {odd}.")
print(f"A lista de números pares ordenada é: {numbers[0]}.")
print(f"A lista de números ímpares ordenada é: {numbers[1]}.")

print("~="*20)
