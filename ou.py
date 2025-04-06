dia = input("Hoje é sábado ou domingo? (s/n): ").lower()
feriado = input("Hoje é feriado? (s/n): ").lower()

if dia == 's' or feriado == 's':
    print("Hoje você pode descansar!")
else:
    print("Hoje é dia útil, bora trabalhar!")
