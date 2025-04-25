from multiprocessing import Process
import math
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end, label):
    print(f"{label}: Counting primes from {start} to {end}")
    count = sum(1 for n in range(start, end) if is_prime(n))
    print(f"{label}: Found {count} prime numbers")

if __name__ == '__main__':
    range_limit = 200_000  # Checking for prime numbers in the range from 2 to 199,999

    start_time = time.time()

    # Create two processes to divide the prime counting workload
    process_1 = Process(target=count_primes, args=(2, range_limit // 2, "Process-1"))
    process_2 = Process(target=count_primes, args=(range_limit // 2, range_limit, "Process-2"))

    # Start both processes
    process_1.start()
    process_2.start()

    # Wait for both processes to finish
    process_1.join()
    process_2.join()

    duration = time.time() - start_time
    print(f"Main process: All subprocesses completed in {duration:.2f} seconds")
