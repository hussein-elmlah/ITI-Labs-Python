# Q1. Function to validate user input as a number
def validate_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input.")

# print("Q1. Function to validate user input as a number")
# validate_number()

# Q2. Check if a number is within the range [20, 50]
def check_number_range():
    number = validate_number()
    if 20 <= number <= 50:
        print("In range.")
    else:
        print("Not in range.")

# print("Q2. Check if a number is within the range [20, 50]")
# check_number_range()

# Q3. Calculate area and perimeter of a rectangle
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    print("Area:", area)
    print("Perimeter:", perimeter)

# print("Q3. Calculate area and perimeter of a rectangle")
# calculate_rectangle_properties(5, 6)

# Q4. Concatenate two strings
def concatenate_strings(string1, string2):
    concatenated_string = string1 + string2
    print("Concatenated string:", concatenated_string)

# print("Q4. Concatenate two strings")
# concatenate_strings("Hello, ", "World!")

# Q5. Square elements in a list
def square_list_elements(*numbers):
    squared_list = [x * x for x in numbers]
    print("Squared list:", squared_list)

# print("Q5. Square elements in a list")
# square_list_elements(1, 2, 3, 4, 5)

# Q6. Merge two dictionaries
def merge_two_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)

# print("Q6. Merge two dictionaries")
# merge_two_dictionaries({"a": 1, "b": 2}, {"c": 3, "d": 4})

# Q7. Merge two lists
def merge_two_lists(list1, list2):
    merged_list = list1 + list2
    print("Merged list:", merged_list)

# print("Q7. Merge two lists")
# merge_two_lists([1, 2, 3], [4, 5, 6])

# Q8. Check if keys exist in a dictionary
def check_keys_exist(dictionary):
    if 'job' in dictionary and 'card_number' in dictionary:
        print("Keys present.")
    else:
        print("Keys not present.")

# print("Q8. Check if keys exist in a dictionary")
# check_keys_exist({"name": "John", "age": 30, "job": "Engineer"})

# Q9. Calculate sum of numbers from 1 to 100
def calculate_sum():
    total = sum(range(1, 101))
    print("Sum of numbers from 1 to 100:", total)

# print("Q9. Calculate sum of numbers from 1 to 100")
# calculate_sum()

# Q10. Check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print("Even.")
    else:
        print("Odd.")

# print("Q10. Check if a number is even or odd")
# check_even_odd(25)

# Q11. Reverse a given string
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    print("Reversed string:", reversed_string)

# print("Q11. Reverse a given string")
# reverse_string("Hello")

# Q12. Check if a string is a palindrome
def is_palindrome(input_string):
    if input_string == input_string[::-1]:
        print("Palindrome.")
    else:
        print("Not a palindrome.")

# print("Q12. Check if a string is a palindrome")
# is_palindrome("racecar")

# Q13. Remove even numbers and square remaining odd numbers in a list
def process_list(input_list):
    processed_list = [x * x for x in input_list if x % 2 != 0]
    print("Processed list:", processed_list)

# print("Q13. Remove even numbers and square remaining odd numbers in a list")
# process_list([1, 2, 3, 4, 5, 6, 7])

# Q14. Check if a number is prime
def is_prime(number):
    if number < 2:
        print("Not prime.")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not prime.")
            return
    print("Prime.")

# print("Q14. Check if a number is prime")
# is_prime(17)

# Q15. Calculate factorial of a number using recursion
def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)

# print("Q15. Calculate factorial of a number using recursion")
# factorial_of_5 = calculate_factorial(5)
# print("Factorial of 5:", factorial_of_5)
