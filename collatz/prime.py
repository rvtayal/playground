import math
import collatz

def is_prime(num):
    if (num < 2):
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


if __name__ == "__main__":
    nums = get_n_primes(50)
    collatz.build_collatz_graph(list(range(2,1000)))