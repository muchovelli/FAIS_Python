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
        print("Wrong input!")
        return False


number = input("Enter a number: ")

