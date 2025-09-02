import random


salary = int(input())
bonus = bool(random.getrandbits(1))
if bonus:
    full_salary = salary + random.randint(1, 100000)
    print(f"{salary}, {bonus} - '{full_salary}'")
else:
    print(f"{salary}, {bonus} - '{salary}'")
