def add_poly(poly1, poly2) -> list:
    size = max(len(poly1), len(poly2))
    sum = [0 for _ in range(size)]

    for i in range(len(poly1)):
        sum[i] = poly1[i]

    for i in range(len(poly2)):
        sum[i] += poly2[i]

    while sum[-1] == 0 and len(sum) > 1:
        sum.pop()

    return sum


def sub_poly(poly1, poly2) -> list:
    size = max(len(poly1), len(poly2))
    sub = [0 for _ in range(size)]

    for i in range(len(poly1)):
        sub[i] = poly1[i]

    for i in range(len(poly2)):
        sub[i] -= poly2[i]

    while sub[-1] == 0 and len(sub) > 1:
        sub.pop()

    return sub


def mul_poly(poly1, poly2) -> list:
    size = (len(poly1) + len(poly2) - 1)
    mul = [0 for _ in range(size)]

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            mul[i + j] += poly1[i] * poly2[j]

    while mul[-1] == 0 and len(mul) > 1:
        mul.pop()

    return mul


def is_zero(poly) -> bool:
    if set(poly) != {0}:
        return False
    else:
        return True


def eq_poly(poly1, poly2) -> bool:
    for poly in [poly1, poly2]:
        while poly[-1] == 0 and len(poly) > 1:
            poly.pop()

    return poly1 == poly2


def eval_poly(poly, x0) -> float:
    result = False
    for i in reversed(poly):
        if not result:
            result = i
            continue
        result = result * x0 + i

    return result


def pow_poly(poly, n) -> list:
    result = [1]
    for i in range(n):
        result = mul_poly(result, poly)

    while result[-1] == 0 and len(result) > 1:
        result.pop()

    return result


def diff_poly(poly) -> list:
    result = []
    for i, x in enumerate(poly):
        if i == 0:
            continue
        result.append(i * x)
    return result

# write a function which sums two polynomials
def add_poly(poly1, poly2):
    result = []
    for i in range(max(len(poly1), len(poly2))):
        if i < len(poly1) and i < len(poly2):
            result.append(poly1[i] + poly2[i])
        elif i < len(poly1):
            result.append(poly1[i])
        else:
            result.append(poly2[i])
    return result

# write a function which takes a polynomial as an argument and returns a new function
def poly_to_fun(poly):
    def fun(x):
        result = 0
        for i, p in enumerate(poly):
            result += p * x ** i
        return result
    return fun