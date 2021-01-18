"""
    Matrix Analysis
"""
print("~="*20)
print(f"{'Análise de Matriz':^40}")
print("~="*20)

numbers = list()
internNumbers = list()
evenTotSum = 0
sumThirdColumn = 0

for i in range(0, 3):
    for j in range(0, 3):
        def inteiro(texto):
            falso = False
            zero = 0
            while True:
                number = str(input(texto))
                if number.isnumeric():
                    zero = int(number)
                    falso = True
                else:
                    print('\033[31m"ERROR!!,DIGITE APENAS NÚMEROS"\033[m')
                if falso:
                    break
            return zero
        number = inteiro(f"Digite um valor para posição[{i}, {j}]: ")
        internNumbers.append(number)
    numbers.append(internNumbers[:])
    del internNumbers[:]

for number in numbers:
    print(f"[ {number[0]} ] [ {number[1]} ] [ {number[2]} ]")
    for eachNumber in number:
        if eachNumber % 2 == 0:
            evenTotSum += eachNumber
    sumThirdColumn += number[2]
higherNumberSecondLine = max(numbers[1])

print(f"A soma dos valores pares é {evenTotSum}.")
print(f"A soma dos valores da terceira coluna é {sumThirdColumn}.")
print(f"O maior valor da segunda linha é {higherNumberSecondLine}.")
print("~="*20)
