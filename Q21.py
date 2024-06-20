Q) Get user input using input(“Enter your age: ”). If user is 18 or older, give‬
‭feedback: You are old enough to drive. If below 18 give feedback to wait for‬
‭the missing amount of years. Output:


Answer:

def check_age_for_driving(age):
    if age >= 18:
        return "You are old enough to drive."
    else:
        return f"You need {18 - age} more years to learn to drive."

print(check_age_for_driving(30))
print(check_age_for_driving(15))


