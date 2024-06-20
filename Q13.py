Q) Declare a function named evens_and_odds . It takes a positive integer as‬ parameter and it counts number of evens and odds in the number.
‭

print(evens_and_odds_(100)
      #The number of odds are 50.
      # The number of evens are 51.


      Answer:

def evens_and_odds(n):
    evens = sum([i for i in range(1, n + 1) if i % 2 == 0])
    odds = sum([i for i in range(1, n + 1) if i % 2 != 0])
    return f"The number of odds are {odds}. The number of evens are {evens}."

print(evens_and_odds(100))





  
