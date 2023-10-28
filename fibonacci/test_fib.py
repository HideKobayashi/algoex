import unittest
import datetime
from typing import Callable
from parameterized import parameterized

from fib import Fib

test_cases = [
    # (1, 1),
    # (2, 1),
    # (3, 2),
    # (4, 3),
    # (5, 5),
    # (6, 8),
    # (7, 13),
    # (8, 21),
    # (9, 34),
    # (10, 55),
    # (11, 89),
    # (12, 144),
    # (13, 233),
    # (14, 377),
    # (15, 610),
    # (16, 987),
    # (17, 1597),
    # (18, 2584),
    # (19, 4181),
    # (20, 6765),
    # (21, 10946),
    # (22, 17711),
    # (23, 28657),
    # (24, 46368),
    # (25, 75025),
    # (26, 121393),
    # (27, 196418),
    # (28, 317811),
    # (29, 514229),
    # (30, 832040),
    # (31, 1346269),
    # (32, 2178309),
    # (33, 3524578),
    # (34, 5702887),
    (35, 9227465),
    (36, 14930352),
    (37, 24157817),
    (38, 39088169),
    (39, 63245986),
    (50, 12586269025),
    (100, 354224848179261915075)
]


def measure_elapsed_time(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        start_dt = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_dt = datetime.datetime.now()
        elapsed_time = end_dt - start_dt
        print("elapsed_time:", elapsed_time)
        return result

    return wrapper


class TestFib1(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.logic = Fib()

    @parameterized.expand([
        (35, 9227465),
    ])
    def test_fibx_ok(self, n, expect):
        func = measure_elapsed_time(self.logic.fibx)
        result = func(n)

        self.assertEqual(result, expect)

    @parameterized.expand([
        (35, 9227465),
    ])
    def test_fib1_ok(self, n, expect):

        func = measure_elapsed_time(self.logic.fib1)
        result = func(n)

        self.assertEqual(result, expect)

    @parameterized.expand([
        (35, 9227465),
    ])
    def test_fib2_ok(self, n, expect):

        func = measure_elapsed_time(self.logic.fib2)
        result = func(n)

        self.assertEqual(result, expect)

    @parameterized.expand([
        (35, 9227465),
    ])
    def test_fib3_ok(self, n, expect):

        func = measure_elapsed_time(self.logic.fib3)
        result = func(n)

        self.assertEqual(result, expect)



