import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion (if using Python 3.11 or later)
sys.set_int_max_str_digits(1000000000)

# Create a function to compute the factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [50, 60, 70]
    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
