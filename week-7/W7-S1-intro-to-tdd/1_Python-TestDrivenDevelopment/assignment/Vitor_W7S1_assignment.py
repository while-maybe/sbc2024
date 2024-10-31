#start writing code from here.
import unittest

# Factorial Calculation:
class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        """test factorials"""
        with self.assertRaises(ValueError):
            factorial(-1)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(9), 362_880)

def factorial(n):
    if n < 0:
        raise ValueError
    if not n:
        return 1
    return n * factorial(n - 1)


# GCD Calculation: gcd(a, b) should compute the greatest common divisor of two integers
class TestGCD(unittest.TestCase):
    def test_gcd(self):
        with self.assertRaises(ValueError):
            cgd(0, 1)
        with self.assertRaises(ValueError):
            cgd(1, 0)
        with self.assertRaises(ValueError):
            cgd(0, 0)
        self.assertEqual(cgd(1, 1), 1)
        self.assertEqual(cgd(10, 20), 10)
        self.assertEqual(cgd(1, -5), 1)
        self.assertEqual(cgd(-1, -5), 1)
        self.assertEqual(cgd(743, 68865), 1)
        self.assertEqual(cgd(3000, 60), 60)
        self.assertEqual(cgd(200, 20), 20)

def cgd(a, b):
    if not a or not b:
        raise ValueError
    # abs below is needed to handle negative numbers
    # divisors_a = {i for i in range(1, abs(a) + 1) if a % i == 0}
    # divisors_b = {i for i in range(1, abs(b) + 1) if b % i == 0}
    # return sorted(divisors_a & divisors_b)[-1]

    while b != 0:
        (a, b) = (b, a % b)
    return abs(a)


# Power Calculation
class testPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(25, -2), 0.0016)
        self.assertEqual(power(4, -2), 0.0625)
        
def power(b, e):
    return b ** e


# Sorted List Check
class testPower(unittest.TestCase):
    def test_is_sorted(self):
        self.assertTrue(is_sorted([1, 2, 3]))
        self.assertTrue(is_sorted([3, 2, 1]))
        self.assertFalse(is_sorted([2, 3, 1]))

def is_sorted(items: list):
    # Exercise doesn't mention sorting order so assuming reversed sorting should also return True
    return items == sorted(items) or items == sorted(items, reverse=True)
    

# Nth Fibonacci Number
class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Write failing tests, then implement function and refactor
        with self.assertRaises(ValueError):
            fibonacci(-1)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(9), 34)

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci hates negative numbers")
    elif n <= 1:
        return n
    else:
       return(fibonacci(n - 1) + fibonacci(n - 2))


# Matrix Addition
class TestMatrixAddition(unittest.TestCase):
    def test_matrix_addition(self):
        self.assertEqual(matrix_addition(
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            
            [[9, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]
            
            ),
                          
            [[10, 10, 10],
             [10, 10, 10],
             [10, 10, 10]]
        )

def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


# Area of Rectangle
class TestAreaRectangle(unittest.TestCase):
    def test_area_rectangle(self):
        # l, w not numeric
        with self.assertRaises(TypeError):
            area_rectangle("a", "b")
        # l, w not numeric
        with self.assertRaises(TypeError):
            area_rectangle("c", 3)
        # l, w zero or less
        with self.assertRaises(ValueError):
            area_rectangle(0, 8.43)
        # l, w zero or less
        with self.assertRaises(ValueError):
            area_rectangle(72, -4)
        # , w are good
        self.assertEqual(area_rectangle(3.5, 2), 7)

def area_rectangle(l, w):
    if not (isinstance(l, (int, float)) and isinstance(w, (int, float))):     
        raise TypeError("Length/Width must be numeric")
    if l <= 0 or w <= 0:
        raise ValueError("Length/Width must be greater than 0")
    return l * w


# Area of Circle
class TestAreaCircle(unittest.TestCase):
    def test_area_circle(self):
        with self.assertRaises(ValueError):
            area_circle(0)
        self.assertAlmostEqual(area_circle(3.24), 32.979183040324)

def area_circle(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be numeric")
    elif radius <= 0:
        raise ValueError("Radius must be greater than 0")
    import math
    return math.pi * radius ** 2


# Perfect Square Check
class TestPerfectSquare(unittest.TestCase):
    def test_perfect_square(self):
        # n not numeric
        with self.assertRaises(TypeError):
            perfect_square("b")
        # n is a float
        with self.assertRaises(TypeError):
            perfect_square("b")
        # n <= 0
        with self.assertRaises(ValueError):
            perfect_square(0)
        # 9 * 9 = 81
        self.assertTrue(perfect_square(81))
        self.assertFalse(perfect_square(80))
        
def perfect_square(n):
    if isinstance(n, (float)):
        raise TypeError("A perfect square can't be a float")
    elif not isinstance(n, (int)):
        raise TypeError("Length/Width must be numeric")
    elif n <=0:
        raise ValueError("Area must be greater than 0")
    else:
        import math
        # isqrt rounds square root to int
        return math.isqrt(n) ** 2 == n


if __name__ == '__main__':
    unittest.main()
