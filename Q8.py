Q) Declare a function named capitalize_list_items. It takes a list as a parameter‬ and it returns a capitalized list of items
‭

Answer:


def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
  print(capitalize_list_items(['cherry', 'banana', 'mango', 'tomato']))
