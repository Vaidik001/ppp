
#Take is list of 10 elements and sum all elements

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum(my_list)
print("The sum of all elements in the list is:", total_sum)



#Take a list of 5 city name and display city having max group

city_names = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
max_length_city = max(city_names, key=len)
print("The city with the maximum length is:", max_length_city)




#Take a list of 10 elemets and remove duplicate elements from that

my_list = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8]
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)




#take a list of 10 hobby and display most appear hobby

from collections import Counter

# Define a list with 10 hobbies, including some duplicates
hobbies = ["reading", "swimming", "reading", "painting", "swimming", "gaming", "gaming", "reading", "cooking", "gaming"]

# Count the occurrences of each hobby
hobby_counts = Counter(hobbies)

# Find the hobby with the maximum count
most_common_hobby = hobby_counts.most_common(1)[0]

# Print the result
print("The most common hobby is:", most_common_hobby[0], "with", most_common_hobby[1], "occurrences")





 #Take a list of 10 elements and display prime no from that

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Define a list with 10 elements
numbers = [2, 4, 6, 7, 11, 13, 15, 18, 19, 21]

# Filter the list to include only prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Print the result
print("Prime numbers in the list are:", prime_numbers)
