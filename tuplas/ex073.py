"""
    List of Paraense Championship
"""
print("~="*20)
print("{:^20}".format("Campeonato Paraense"))
print("~="*20)
generalClassification = ("Remo",
    "Paysandu",
    "Bragantino",
    "São Raimundo-PA",
    "Castanhal",
    "Independente",
    "Aguia de Marabá",
    "Paragominas",
    "Parauapebas",
    "Cametá"
)
print("Primeiros cinco colocados são:")
print(f"{generalClassification[:5]}")
print("-"*40)
print("Quatro últimos colocados são:")
print(f"{generalClassification[-4:]}")
print("-"*40)
print("Lista em oredem alfabética:")
print(f"{sorted(generalClassification)}")
print("-"*40)
for pos, time in enumerate(generalClassification):
    if time == "Aguia de Marabá":
        print(f"O Águia de Marabá está na posição {pos} da tabela do Paraense.")
print("~="*20)
