# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    num = 1
    while n > 0:
        num = num * n
        n = n - 1
    return num


if __name__ == "__main__":
    n = int(input("Podaj liczbe podstawy silni: "))
    print(factorial(n))
