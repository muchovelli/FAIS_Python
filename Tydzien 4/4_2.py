# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane,
# tylko korzystać z argumentów.


def make_ruler(length):
    temp = "|..."
    top = temp * length + "|"
    bot = ""

    for i in range(0, length + 1):
        if i < 9:
            bot += str(i) + "   "
        else:
            bot += str(i) + "  "

    ruler = top + "\n" + bot
    return ruler


def make_grid(x, y):
    result = ""

    for i in range(0, y):
        result = result + "+---" * x + "+\n"
        result = result + "|   " * x + "|\n"

    result = result + "+---" * x + "+\n"
    return result


if __name__ == "__main__":
    _len = int(input("Podaj dlugosc linijki: "))
    print(make_ruler(_len))
    x = int(input("Podaj szerokosc: "))
    y = int(input("Podaj wysokosc: "))
    print(make_grid(x, y))
