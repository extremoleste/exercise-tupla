"""
    Report Card
"""
from statistics import mean

print("~="*20)
print(f"{'BOLETIM':^40}")
print("~="*20)

students = list()
choiceStudent = 0

while True:
    name = str(input("Nome: ")).strip()
    grade1 = float(input("Nota 1: "))
    grade2 = float(input("Nota 2: "))
    students.append([name, [grade1, grade2]])
    while True:
        continuous = str(input("Deseja continuar [s/n]: ")).strip().lower()
        if continuous in "sn":
            break
    if continuous == "n":
        break

print("~="*20)
print(f"{'No. ':<8} {'NOME':<20} {'MÉDIA':>5}")
print("-"*40)
for pos, student in enumerate(students):
    print(f"{pos:<8} {student[0]:<20} {mean(student[1]):>5}")
print("-"*40)

while True:
    choiceStudent = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    if choiceStudent == 999:
        break
    print(f"Notas de {students[choiceStudent][0]} são {students[choiceStudent][1]}.")
    print("-"*40)
print("~="*20)
