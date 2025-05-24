cars = ["bmw", "audi", "mercedes", "toyota", "ford", "honda", "nissan", "chevrolet", "hyundai", "kia"]

text = ""
i = 0
while i < len(cars):
    text += f"{cars[i]}\n"
    i += 1

print(text)
