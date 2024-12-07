import unittest
from fraction import Fraction


class FractionTestCase(unittest.TestCase):

    def test_initialization(self):
        """Test de l'initialisation et de la simplification des fractions"""
        f = Fraction(4, 8)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        with self.assertRaises(ValueError):
            Fraction(1, 0)  # Test pour le dénominateur 0

        with self.assertRaises(ValueError):
            Fraction(1.5, 3)  # Test pour un numérateur non entier

        with self.assertRaises(ValueError):
            Fraction(3, "den")  # Test pour un dénominateur non entier

    def test_string_representation(self):
        """Test des représentations textuelles"""
        self.assertEqual(str(Fraction(1, 2)), "1 / 2")
        self.assertEqual(str(Fraction(3, 1)), "3")

    def test_mixed_number(self):
        """Test de la conversion en nombre mixte"""
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2+1/3")
        self.assertEqual(Fraction(3, 2).as_mixed_number(), "1+1/2")
        self.assertEqual(Fraction(2, 3).as_mixed_number(), "2/3")

    def test_addition(self):
        """Test de l'opérateur +"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6))

    def test_subtraction(self):
        """Test de l'opérateur -"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 - f2, Fraction(1, 6))

    def test_multiplication(self):
        """Test de l'opérateur *"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(1, 2))

    def test_division(self):
        """Test de l'opérateur /"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 / f2, Fraction(8, 9))

        with self.assertRaises(ValueError):
            f1 / Fraction(0, 1)

    def test_equality(self):
        """Test de l'opérateur =="""
        self.assertTrue(Fraction(2, 3) == Fraction(4, 6))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))

    def test_float_conversion(self):
        """Test de la conversion en float"""
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(2, 3)), 2 / 3)

    def test_properties(self):
        """Test des propriétés is_zero, is_integer, is_proper, is_unit"""
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertTrue(Fraction(1, 3).is_unit())
    def test_is_adjacent_to(self):
        """Test de la méthode is_adjacent_to"""
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(5, 6)))
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(4, 3)))
if __name__ == "__main__":
    unittest.main()