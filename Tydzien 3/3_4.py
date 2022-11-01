# Napisać program pobierający w pętli od użytkownika
# liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
import re


def checkIfNumeric(number):
    try:
        float(number)
        return True
    except ValueError:
        print("Zly input!")
        return False


while True:
    number = input("Podaj liczbe: ")
    if checkIfNumeric(number):
        print("Podstawa: %s.\nWynik: %s" % (float(number), float(number) * float(number)))
    elif number == "stop":
        print("Koniec")
        break
    else:
        continue
