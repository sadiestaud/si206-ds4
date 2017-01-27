import unittest
# function to return the factorial of a number
# Add comments
def factorial(num):
    ans = 1
    if num < 0:
        return None
    elif num < 2:
        return ans
    else:
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                isLeap = True
        else:
            isLeap = True
    return isLeap

# print("factorial(0): {}".format(factorial(0)))
# print("factorial(1): {}".format(factorial(1)))
# print("factorial(5): {}".format(factorial(5)))
# print("factorial(-3): {}".format(factorial(-3)))

# print("check_leap_year(2000): {}".format(check_leap_year(2000)))
# print("check_leap_year(1990): {}".format(check_leap_year(1990)))
# print("check_leap_year(2012): {}".format(check_leap_year(2012)))
# print("check_leap_year(2100): {}".format(check_leap_year(2100)))

class TestCases(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(factorial(0), 1, "testing that 0 will return 1")
    def test_f2(self):
        self.assertEqual(factorial(1), 1, "testing that the value 1 will return 1")
    def test_f3(self):
        self.assertEqual(factorial(-5), None, "testing that the value -5 will return None")
    def test_f4(self):
        self.assertEqual(factorial(5), 120, "testing that the value 5 will return 120")
    def test_ly1(self):
        self.assertEqual(check_leap_year(1900), False, "testing that 1900 will return false")
    def test_ly2(self):
        self.assertEqual(check_leap_year(1912), True, "testing that 1912 will return true")
    def test_ly3(self):
        self.assertEqual(check_leap_year(2000), True, "testing that 2000 will return true")






unittest.main(verbosity=2) 



