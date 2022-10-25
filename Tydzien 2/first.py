# Zadanie 2.10
print('\nZadanie 2.10')
line1 = 'Tutaj mamy \tcztery\nwyrazy'
result1 = line1.split()
print(len(result1))

# Zadanie 2.11
print('\nZadanie 2.11')
line2 = 'word'
result2 = '_'.join(line2)
print(result2)

# Zadanie 2.12
print('\nZadanie 2.12')
line3 = 'Zdanie ktore pomoze nam zrobic slowa'
splittedLine3 = line3.split()

first = ""
last = ""
for c in splittedLine3:
    first += c[0]
    last += c[-1:]

print(first)
print(last)

# Zadanie 2.13
print('\nZadanie 2.13')
line4 = 'Zdanie ktore\t\n pomoze nam zrobic slowa'
splittedLine4 = line4.split()
result4 = sum(len(c) for c in splittedLine4)
print(result4)

# Zadanie 2.14
print('\nZadanie 2.14')
line5 = 'Zdanie ktore\t\n pomoze nam zrobic slowa'
lineSplitted5 = line5.split()

word5 = ''
max5 = 0
for c in lineSplitted5:
    if max5 <= len(c):
        max5 = len(c)
        word5 = c

print(word5)
print(max5)

# Zadanie 2.15
print('\nZadanie 2.15')
L = [12, 42, 12, 12, 1, 21, 12, 2]

result6 = ''.join(str(i) for i in L)
print(result6)

# Zadanie 2.16
print('\nZadanie 2.16')
line7 = 'GvR is a Dutch programmer'

result7 = line7.replace('GvR', 'Guido van Rossum')
print(result7)

# Zadanie 2.17
print('\nZadanie 2.17')
line8 = 'Guido van Rossum is a Dutch programmer'

abc8 = sorted(line8.split())
len8 = sorted(line8.split(), key=len)

print(abc8)
print(len8)

# Zadanie 2.18
print('\nZadanie 2.18')
number9 = 1230213042143590342324023053204230402304023400230420340205034050340564056034052340235023050230502305403

result9 = str(number9).count('0')
print(result9)

# Zadanie 2.19
print("\nZadanie 2.19")
L = [12, 42, 12, 12, 1, 21, 12, 2, 900, 120, 123]

result10 = ' '.join(str(i).zfill(3) for i in L)
print(result10)
