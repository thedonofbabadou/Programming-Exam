# Question 1

a = 10
a = a + 2
print(a * 2)

a = 19
print(a + 3)

a = a // 2

print("Final value of a:", a)

# Question 2

result = 2 + 3 * 6 / 2
# 3 * 6 = 18, then 18 / 2 = 9.0, then 2 + 9.0 = 11.0
print("Result of the expression:", result)

# Question 3

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month

a = a + day_of_week
b += month_of_year

print(a)
print(b)

c = a + b
print(c)

d = "abc" * (c // 3)
print(d)


# Question 4

def palindrome(word):
    if word == word[::-1]:  # Checks if the word is the same when reversed
        return True
    else:
        return False

# List of numbers to check
numbers = [
    "6892149109325320763773670235239019412986",
    "9847255590886266818998186626880955527489",
    "6800923757255865070000705685527573290086",
    "1414884937242655719669145562427394884141"
]

# Check each number and print whether it's a palindrome
for number in numbers:
    if palindrome(number):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is NOT a palindrome")

# Question 5

def find_unan_patterns(text):
    count = 0
    start = 0

    while True:

        start = text.find("un", start)
        if start == -1:
            break


        end = text.find("an", start + 2)
        if end != -1:
            count += 1
            start = end + 2
        else:
            break

    return count

# Question 6

# Example of a mutable list
my_list = [1, 2, 3, 4]
my_list[1] = 20
my_list.append(5)
print(my_list)

# Example of an immutable string
my_string = "hello"
# my_string[0] = "y"  # This would cause an error because strings are immutable
new_string = "y" + my_string[1:]
print(new_string)

# Question 7

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

new_numbers = []

for number in random_numbers:
    if number % 2 == 0:
        new_numbers.append(number * 2)

print("Original list:", random_numbers)
print("Processed list:", new_numbers)

# Question 8

def is_valid_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    if url.startswith("http://"):
        domain = url[7:]
    else:
        domain = url[8:]

    if '.' not in domain:
        return False

    dot_index = domain.rfind('.')
    if dot_index == len(domain) - 1:
        return False

    return True

# Question 9

def days_passed(birthday):
    birth_year = int(birthday[-4:])
    current_year = 2025
    full_years = current_year - birth_year - 1
    total_days = full_years * 365
    return total_days

print(days_passed("05-11-2003"))


