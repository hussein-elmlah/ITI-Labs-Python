import json
import math

numbers = [4, 9, 16, 25, 36]

sqrt_nums = list(map(lambda x: math.sqrt(x), numbers))

data = dict(zip(numbers, sqrt_nums))

with open('sqrt_numbers.json', 'w') as file:
    json.dump(data, file)

print("Square roots saved to sqrt_numbers.json:", data)
