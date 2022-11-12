# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją,
# wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):
    if isinstance(sequence, (list, tuple)):
        result = []
        for item in sequence:
            result.extend(flatten(item))
        return result
    else:
        return [sequence]


if __name__ == "__main__":
    seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print("Sekwencja: ")
    print(seq)
    print("Splaszczona sekwencja: ")
    print(flatten(seq))
