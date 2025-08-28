baskara.py
import math

# Coeficientes da equação: ax² + bx + c = 0
a = 1
b = -3
c = -4

# Calculando o delta
delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    # Fórmula de Bhaskara
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("As raízes da equação são:")
    print("x1 =", x1)
    print("x2 =", x2)
