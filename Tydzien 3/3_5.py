# Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.

chunk = "|..."
length = int(input("Podaj dlugosc miarki: "))
print(chunk * length + "|")

for i in range(length + 1):
    if i >= 9:
        print(i, end='')
        print("  ", end='')
    else:
        print(i, end='')
        print("   ", end='')
