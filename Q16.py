Q) Write a function which checks if all the items of the list are of the same data‬ type.
‭


Answer:

def check_data_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

print(check_data_type([1, 2, 3, 4, 5]))
print(check_data_type(['a', 'b', 'c', 'd', 'e']))









