# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

# 1. Read the number of items (N)
N = int(input())

# 2. Read the actual numbers into a list
numbers = list(map(int, input().split()))

# 3. Create a counter for how many primes we find
prime_count = 0

# 4. Check every single number in our list
for num in numbers:
    # Trap check: 1 and 0 are not prime numbers!
    if num < 2:
        continue 
    
    # Assume the number is prime until proven otherwise
    is_prime = True
    
    # Try dividing 'num' by every number from 2 up to (num - 1)
    for i in range(2, num):
        if num % i == 0:
            # We found a number that divides evenly into it! 
            # It is NOT a prime number.
            is_prime = False
            break  # Stop checking and break out of this inner loop
            
    # If we checked all the numbers and didn't find any divisors, it's prime!
    if is_prime == True:
        prime_count += 1

# 5. Print the final count of prime numbers
print(prime_count)
