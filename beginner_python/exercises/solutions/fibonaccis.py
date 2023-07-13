from functools import lru_cache
from datetime import datetime

NUM_TIMES = 35


# Part 1
def fibonacci(n):
    """
    Simple, but slow recursive fibonacci
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# takes a really long time
start_time = datetime.now()
fibonacci(NUM_TIMES)
end_time = datetime.now()
print(f"it took {(end_time-start_time).total_seconds()}")


# Part 2
@lru_cache
def fibonacci_cached(n):
    """
    This function is exactly the same as `fibonacci`,
    but it uses `functools.lru_cache`, leading to
    huge speedups
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


# much faster now
start_time = datetime.now()
fibonacci_cached(NUM_TIMES)
end_time = datetime.now()
print(f"it took {(end_time-start_time).total_seconds()}")


# Part 3
def fibonacci_dynamic(n):
    """
    Instead of recursively calling itself,
    this function solves for the nth fibonacci
    term using dynamic programming
    """
    if n <= 0:
        return 0
    if n <= 2:
        return 1

    term_num = 1
    cur = 1
    prev = 0

    while term_num < n:
        cur, prev = cur + prev, cur
        term_num += 1


# also super fast
start_time = datetime.now()
fibonacci_dynamic(NUM_TIMES)
end_time = datetime.now()
print(f"it took {(end_time-start_time).total_seconds()}")
