Q) Write a function called check-season, it takes a month parameter and returns‬ the season: Autumn, Winter, Spring or Summer.


Answer : 

def check_season(month):
    if month in [5, 2, 7]:
        return "Spring"
    elif month in [4, 7, 5]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Winter"

print(check_season(5))


‭
