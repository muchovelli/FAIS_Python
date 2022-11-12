# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
# która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).


def sum_seq(sequence):
    if isinstance(sequence, (list, tuple)):
        return sum(map(sum_seq, sequence))
    return sequence


if __name__ == "__main__":
    seq = [1, [], (2, 3), [4, (5, 6, 7)], 8, [9]]
    print("Sekwencja: ")
    print(seq)
    print("Suma: ")
    print(str(sum_seq(seq)))
