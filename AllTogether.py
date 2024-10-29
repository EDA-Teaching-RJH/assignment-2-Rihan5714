import random
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list of random numbers:", random_numbers)
index = 0
while index < len(random_numbers):
    if random_numbers[index] % 2 == 0:  # Check if the number is even
        random_numbers.pop(index)  # Remove the even number
    else:
        index += 1  # Only increment the index if no item is removed 
print("Remaining odd numbers:", random_numbers)
