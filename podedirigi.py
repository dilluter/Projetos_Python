idade = 7 ** 3
if idade >= 100:
    dirigir = "está incapacitado"
elif idade >= 18:
    dirigir = "pode dirigir"
else:
    dirigir = "não pode dirigir"
print(f"A pessoa tem {idade} anos, logo {dirigir}.")
