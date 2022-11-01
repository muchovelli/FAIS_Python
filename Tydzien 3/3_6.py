width = int(input("Podaj szerokosc: "))
height = int(input("Podaj wysokosc: "))
result = ""

for i in range(0, height):
    result = result + "+---" * width + "+\n"
    result = result + "|   " * width + "|\n"

result = result + "+---" * width + "+\n"
print(result)
