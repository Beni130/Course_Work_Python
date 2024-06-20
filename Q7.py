Q) ‭Declare a function named reverse_list. It takes an array as a parameter and it‬ returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

Answer:


def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A', 'B', 'C']))

‭
