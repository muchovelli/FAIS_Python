# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru
# left do right włącznie. Lista jest modyfikowana w miejscu (in place).
# Rozważyć wersję iteracyjną i rekurencyjną.


def iter(L, left, right):
    0
    while right != left:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        right = right - 1
        left = left + 1
    return L


def recu(L, left, right):
    if left != right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        L = recu(L, left + 1, right - 1)
    return L


if __name__ == "__main__":
    list = [7, 4, 12, 4, 7, 8, 1, 3, 44]
    print("Przed Odwroceniem: ")
    print(list)

    print("Po rotacji iteracyjnie: ")
    print(iter(list, 0, 8))

    print("Po rotacji rekurencyjnie: ")
    print(recu(list, 0, 8))
