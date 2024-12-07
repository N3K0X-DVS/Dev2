from fraction import Fraction

if __name__ == '__main__':
    f = Fraction(5, 2)
    f2 = Fraction(7, 2)
    print(f)

    print(f2)

    print(f.__repr__())

    print(f.as_mixed_number())

    print(f.is_adjacent_to(f2))

    print(f.is_integer())

    print(f.__add__(f2))

    print(f.__sub__(f2))

    print(f.__mul__(f2))