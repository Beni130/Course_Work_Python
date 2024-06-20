Q) Write a function called is_prime, which checks if a number is prime.




  Answer:

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(6))



  
