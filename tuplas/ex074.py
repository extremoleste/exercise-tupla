"""
    Return five random numbers
"""
from random import sample

numbers = sample(range(10), 5)

print("~="*22)
print("{:^10}".format("Maior e menor número de uma lista aleatória"))
print("~="*22)
print(f"Lista gerada é {numbers}")
print(f"Maior número: {max(numbers)}")
print(f"Menor número: {min(numbers)}")
print("~="*22)
