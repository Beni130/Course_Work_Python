Q) Write a function which generates a six digit/character random_user_id. print‬(randomu_user_id());
"lee33d"

Answer:

import random
import string

def random_user_id():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

print(random_user_id())




‭
