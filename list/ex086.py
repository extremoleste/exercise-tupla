"""
    Matrix
"""
print("~="*20)
print(f"{'Matriz':^40}")
print("~="*20)

numbers = list()
internNumbers = list()

for i in range(0, 3):
    for j in range(0, 3):
        number = int(input(f"Digite um valor para posição[{i}, {j}]: "))
        internNumbers.append(number)
    numbers.append(internNumbers[:])
    del internNumbers[:]

for number in numbers:
        print(f"[ {number[0]} ] [ {number[1]} ] [ {number[2]} ]")

print("~="*20)
