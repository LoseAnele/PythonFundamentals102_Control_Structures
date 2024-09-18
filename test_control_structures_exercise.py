import unittest
from control_structures_exercise import (categorize_age, is_leap_year, print_numbers_for_loop, print_numbers_while_loop, print_odd_numbers, multiplication_table) 

class Test(unittest.TestCase):

    # Test for Exercise 1 - Age Categorization
    def test_categorize_age(self):
        self.assertEqual(categorize_age(17), "You are a minor.")
        self.assertEqual(categorize_age(25), "You are an adult.")
        self.assertEqual(categorize_age(70), "You are a senior citizen.")

    # Test for Exercise 2 - Leap Year
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2020))  # 2020 is a leap year
        self.assertFalse(is_leap_year(1900))  # 1900 is not a leap year
        self.assertTrue(is_leap_year(2000))  # 2000 is a leap year
        self.assertFalse(is_leap_year(2021))  # 2021 is not a leap year

    # Test for Exercise 3 - Print Numbers with For Loop
    def test_print_numbers_for_loop(self):
        self.assertEqual(print_numbers_for_loop(5), [1, 2, 3, 4, 5])

     # Test for Exercise 4 - Print Numbers with While Loop
    def test_print_numbers_while_loop(self):
        self.assertEqual(print_numbers_while_loop(5), [1, 2, 3, 4, 5])

    # Test for Exercise 5 - Print Odd Numbers
    def test_print_odd_numbers(self):
        self.assertEqual(print_odd_numbers(7), [1, 3, 5, 7])

    # Test for Exercise 6 - Multiplication Table
    def test_multiplication_table(self):
        expected_output = [
            '1 x 1 = 1',
            '2 x 1 = 2',
            '3 x 1 = 3',
            '4 x 1 = 4',
            '5 x 1 = 5',
            '6 x 1 = 6',
            '7 x 1 = 7',
            '8 x 1 = 8',
            '9 x 1 = 9',
            '10 x 1 = 10'
        ]
        self.assertEqual(multiplication_table(1), expected_output)


# Run the tests
if __name__ == '__main__':
    unittest.main()