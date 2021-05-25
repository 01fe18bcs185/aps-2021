# Count the number of prime numbers less than a non-negative number, n.
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def countPrimes(n):
    if n <= 2:
        return 0
    
    non_primes = set()
    
    for num in range(2, int(sqrt(n))+1):
        if num not in non_primes:
            for p in range(num*num, n, num):
                non_primes.add(p)
    
    return n - len(non_primes) - 2 # exclude num and 1
    
print(countPrimes(10))
