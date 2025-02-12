import unittest
from ..my_calculations import Calculations


class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.calculation = Calculations(8, 2)

    def tearDown(self):
        del self.calculation

    def not_a_test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, "The sum is wrong.")

    @unittest.skip("saltando un test")
    def test_nothing(self):
        self.fail("Nada va pasar")

    def test_sum(self):
        """
        Test that sum two numbers
        """
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10.0, "The sum is wrong.")

    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, "The difference is wrong.")

    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, "The product is wrong.")

    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, "The quotient is wrong.")

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "Esto es un error esperado")

    @unittest.skip("pendiente ajustar")
    def test_bad_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(
                self.calculation.get_quotient(), 4, "The result is not a number."
            )


if __name__ == "__main__":
    unittest.main()