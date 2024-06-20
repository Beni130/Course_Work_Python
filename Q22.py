Q) ‭Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

Answer:

def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

print(calculate_grade(80))
print(calculate_grade(70))
print(calculate_grade(60))
print(calculate_grade(50))
print(calculate_grade(0))
