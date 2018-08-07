"""
    Radom numbers in grew order
"""
print("~="*20)
print(f"{'Números aleatórios em ordem crescente':^40}")
print("~="*20)

numbers = []

while True:
    number = int(input("Digite um valor: "))
    while number in numbers:
        print(f"\033[0:30:41mValor {number} já adiciona!\033[m")
        number = int(input("\033[1:33mDigite outro valor:\033[m"))
    print("\033[0:32mValor adicionado com sucesso!\033[m")
    numbers.append(number)
    print("-"*40)
    continuos = str(input("Deseja continuar [s/n]: ")).lower()
    print("-"*40)
    if continuos in "n":
        break

print(f"Os valores digitados foram: {sorted(numbers)}")
print("~="*20)
