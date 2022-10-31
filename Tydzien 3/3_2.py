#Co jest złego w kodzie:

L = [3, 5, 4];
L = L.sort()
#Funkcja sort nie zwraca niczego, po prostu l.sort() powinno byc

x, y = 1, 2, 3
#Nie mozna zadeklarowac 3 wartosci do 2 zmiennych

X = 1, 2, 3 ; X[1] = 4
#Nie mozna zmieniac elementow w tupli

X = [1, 2, 3]; X[3] = 4
#Wstawianie poza liste

X = "abc" ; X.append("d")
#Nie mozna uzyc .append do stringa

L = list(map(pow, range(8)))
#Złe użycie funkcji pow