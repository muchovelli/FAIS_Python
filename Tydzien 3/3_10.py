def roman2int(number):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(number)):
        if i + 1 < len(number) and roman[number[i]] < roman[number[i + 1]]:
            result = result - roman[number[i]]
        else:
            result = result + roman[number[i]]
    return result


x = input("Podaj liczbe: ")
print(roman2int(x))
