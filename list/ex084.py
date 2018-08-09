"""
    Analysis of persons haevier and lighter
"""
print("~="*20)
print(f"{'Análise de Pessoas mais Pesadas e mais Lever':^40}")
print("~="*20)

persons = list()
heaviersNames = list()
heaviersWeight = list()
lightersNames = list()
lightersWeight = list()

while True:
    name = str(input("Nome: ")).strip()
    weight = int(input("Peso: "))
    persons.append([name, weight])
    while True:
        continuous = str(input("Deseja continuar [s/n]: ")).strip().lower()
        if continuous in "sn":
            break
    if continuous == "n":
        break

for i in range(0, len(persons)):
    if persons[i][1] <= 70:
        heaviersNames.append(persons[i][0])
        heaviersWeight.append(f"{str(persons[i][1])}kg")
    if persons[i][1] >= 100:
        lightersNames.append(persons[i][0])
        lightersWeight.append(f"{str(persons[i][1])}kg")

print(f"Ao todo, você cadastrou {len(persons)} pessoas.")
print(f"As pessoas a cima de 100kg têm {', '.join(heaviersWeight)} e são respectivamente {', '.join(heaviersNames)}.")
print(f"As pessoas a baixo de 70kg têm {', '.join(lightersWeight)} e são respectivamente {', '.join(lightersNames)}.")
print("~="*20)
