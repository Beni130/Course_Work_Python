Q) Declare a function named sum_of_odds. It takes a number parameter and it‬ adds all the odd numbers in that range.
‭


Answer:

def sum_of_odds(n):
    return sum([i for i in range(1, n + 1) if i % 2 != 0])

print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))






