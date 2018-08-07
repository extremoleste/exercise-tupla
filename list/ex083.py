"""
    Expression Analysis
"""
print("~="*20)
print(f"{'Análise de Expressão':^40}")
print("~="*20)

expression = str(input("Digite a expressão matemática: "))

parenthesesOpen = expression.count("(")
parenthesesClosed = expression.count(")")

if parenthesesOpen == parenthesesClosed:
    print("\033[0:32mExpressão válida!\033[m")
else:
    print("\033[0:31mExpressão válida!\033[m")

print("~="*20)
