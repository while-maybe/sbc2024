import unittest

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        """_summary_"""
        self.assertTrue(is_palindrome("abcba"))
        """edge cases"""
        self.assertFalse(is_palindrome(""))

def is_palindrome(value: str) -> bool:
    if not value:
        return False
    return value == value[::-1]


class TestPalindrome(unittest.TestCase):
    def test_is_alpha(self):
        self.assertTrue(is_alpha("abc"))
        self.assertFalse(is_alpha("abc1"))
        """edge cases"""
        self.assertFalse(is_alpha(""))
        self.assertFalse(is_alpha("_"))

def is_alpha(value: str) -> bool:
    return value.isalpha()


# Basic Math Operations
def add(a, b):
    # Code for addition
    return a + b

def multiply(a, b):
    # Code for multiplication
    return a * b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # Write failing tests, then implement function and refactor
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(5, -5), 0)
        self.assertEqual(add(-5, -5), -10)
        """edge cases"""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)

        
    def test_multiply(self):
        # Write failing tests, then implement function and refactor
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-5, 5), -25)
        self.assertEqual(multiply(5, -5), -25)
        self.assertEqual(multiply(-5, -5), 25)
        "edge cases"
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(5, 1), 5)


# Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Write failing tests, then implement function and refactor
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(9), 34)

# Anagram Check
def is_anagram(s1, s2):
    # Code for checking anagrams
    return sorted(s1.lower()) == sorted(s2.lower())


class TestAnagram(unittest.TestCase):
    def test_is_anagram(self):
        # Write failing tests, then implement function and refactor
        self.assertTrue(is_anagram("race", "Care"), True)



if __name__ == '__main__':
    unittest.main()
