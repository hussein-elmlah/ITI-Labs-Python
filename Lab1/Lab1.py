# Function to validate user input as a number
def validate_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input.")

# Q1. Check if a number is within the range [20, 50]
def check_number_range():
    number = validate_number()
    if 20 <= number <= 50:
        print("In range.")
    else:
        print("Not in range.")

# Q2. Calculate area and perimeter of a rectangle
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    print("Area:", area)
    print("Perimeter:", perimeter)

# Q3. Concatenate two strings
def concatenate_strings(string1, string2):
    concatenated_string = string1 + string2
    print("Concatenated string:", concatenated_string)

# Q4. Square elements in a list
def square_list_elements(*numbers):
    squared_list = [x * x for x in numbers]
    print("Squared list:", squared_list)

# Q5. Merge two dictionaries
def merge_two_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)

# Q6. Merge two lists
def merge_two_lists(list1, list2):
    merged_list = list1 + list2
    print("Merged list:", merged_list)

# Q7. Check if keys exist in a dictionary
def check_keys_in_dictionary(dictionary):
    if 'job' in dictionary and 'card_number' in dictionary:
        print("Keys present.")
    else:
        print("Keys not present.")

# Q8. Calculate sum of numbers from 1 to 100
def calculate_sum_of_numbers():
    total = sum(range(1, 101))
    print("Sum of numbers from 1 to 100:", total)

# Q9. Check if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        print("Even.")
    else:
        print("Odd.")

# Q10. Reverse a given string
def reverse_given_string(input_string):
    reversed_string = input_string[::-1]
    print("Reversed string:", reversed_string)

# Q11. Check if a string is a palindrome
def is_string_palindrome(input_string):
    if input_string == input_string[::-1]:
        print("Palindrome.")
    else:
        print("Not a palindrome.")

# Q12. Remove even numbers and square remaining odd numbers in a list
def process_list_of_numbers(input_list):
    processed_list = [x * x for x in input_list if x % 2 != 0]
    print("Processed list:", processed_list)

# Q13. Check if a number is prime
def is_number_prime(number):
    if number < 2:
        print("Not prime.")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not prime.")
            return
    print("Prime.")

# Q14. Calculate factorial of a number
def calculate_number_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial:", factorial)

# Q15. Perform various operations on a list of numbers
def perform_operations_on_numbers(numbers):
    results = {
        'sum': sum(numbers),
        'minimum': min(numbers),
        'maximum': max(numbers),
        'squared_list': [num ** 2 for num in numbers]
    }
    print("Operations:", results)

