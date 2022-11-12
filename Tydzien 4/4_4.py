# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    result = 0
    y = 1
    for i in range(0, n):
        last = result
        result = y
        y = last + y
    return result


if __name__ == "__main__":
    n = int(input("Podaj liczbe dla obliczenia funkcji fibonacciego: "))
    print(fibonacci(n))
