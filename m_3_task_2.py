import random

def get_numbers_ticket(min, max, quantity):
    numbers = []

    while len(numbers) < quantity:
        try:
          random_number = random.randint(min, max)
        except TypeError:
            return [] 
        if random_number not in numbers:
            numbers.append(random_number)
    numbers.sort()
    return numbers

lottery_numbers = get_numbers_ticket(1, 40, 6)
print("Ваші лотерейні числа:", lottery_numbers)