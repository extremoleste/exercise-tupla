"""
	Identify number netween 0 - 20
	Translate to word
"""
print("~="*20)
print("{:^20}".format("Numeral para Extenso"))
print("~="*20)
numbers = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Duatorze", "Duinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
	userChoice = int(input("Escolha um número entre 0 e 20: "))
	if userChoice >= 0 and userChoice <=20:
		break
print(f"O número {userChoice} por extenso é {numbers[userChoice]}")
print("~="*20)
