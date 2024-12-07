from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den != 0
        POST : None
        """
        if not (isinstance(num, int) and isinstance(den, int)):
            raise ValueError("Numerator and denominator must be integers")

        if den == 0:
            raise ValueError('denominator is equal to 0')

        pgcd = gcd(num, den)

        self.num = num // pgcd
        self.den = den // pgcd

    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : The string value of the Fraction
        """

        if self.den == 1: return str(self.num)
        return f'{self.num} / {self.den}'

    def __repr__(self):
        if self.den == 1: return str(self.num)
        return f'Fraction(num={self.num}, den={self.den})'

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None
        POST : return the mixed number
        """
        whole_number = self.num // self.den
        remainder = self.num % self.den

        return f'{whole_number}+{remainder}/{self.den}' if whole_number else f'{remainder}/{self.den}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : a Fraction object
         POST : a new Fraction object with value = F1 + F2
         """

        num1 = self.num

        num2 = other.num

        den_commun = self.den

        if self.den != other.den:
            num1 *= other.den
            num2 *= self.den

            den_commun = self.den * other.den

        return Fraction(num=num1 + num2, den=den_commun)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : a Fraction object
        POST : a new Fraction with value of F1 - F2
        """
        num1 = self.num

        num2 = other.num

        den_commun = self.den

        if self.den != other.den:
            num1 *= other.den
            num2 *= self.den

            den_commun = self.den * other.den

        return Fraction(num=num1 - num2, den=den_commun)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : a Fraction object
        POST : a new Fraction object with value of F1 * F2
        """
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : a Fraction object with numerator != 0
        POST : a new Fraction object with value of F1 / F2
        """
        return Fraction(self.num * other.den, self.den * other.num)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : a Fraction object
        POST : a new Fraction object with value of F1 ** F2
        """
        f = (self.num / self.den) ** (other.num / other.den)
        f = f.as_integer_ratio()
        return Fraction(f[0], f[1])

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : a Fraction object
        POST : a boolean

        """
        return self.num / self.den == other.num / other.den

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None
        POST : the float representation
        """
        return self.num / self.den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None
        POST : a boolean
        """
        return self.num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None
        POST : boolean
        """

        f = float(self)
        f = str(f)
        if f.endswith('.0'):
            return True
        return False

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None
        POST : boolean
        """

        return abs(float(self)) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None
        POST : boolean
        """
        return abs(self.num) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : a Fraction object
        POST : boolean
        """
        return (self-other).is_unit()
