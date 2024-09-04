# Exercise 1: Create a Dictionary
person = {"Name": "Alice", "Age": 25, "City": "New York"}
print(person)

# Exercise 2: Access Dictionary Elements
print(person["City"])

# Exercise 3: Add and Modify Elements
person["email"] = "alice@example.com"
person["Age"] = 26
print(person)

# Exercise 4: Remove Elements
del person["City"]
print(person)

# Exercise 5: Check if a Key Exists
if "email" in person:
    print("The key 'email' exists in dict")
else:
    print("The key 'email' does not exist in dict")

if "phone" in person:
    print("The key 'phone' exists in the dict")
else:
    print("The key 'phone' does not exist in dict")

# Exercise 6
person = {"Name": "Alice", "Age": 26, "email": "alice@example.com"}

# 1. Iterate over the person dictionary and print each key-value pair.
for key, value in person.items():
    print(f"{key}: {value}")

# 2. Iterate over the keys of the dictionary and print each key.
for key in person.keys():
    print(key)

# 3. Iterate over the values of the dictionary and print each value.
for value in person.values():
    print(value)



# Exercise 7: Nested Dictionary
employees = {
    101: {"name": "Bob", "job": "Engineer"},
    102: {"name": "Sue", "job": "Designer"},
    103: {"name": "Tom", "job": "Manager"}
}
print(employees[102])

employees[104] = {"name": "Linda", "job": "HR"}
print(employees)

# Exercise 8: Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Exercise 9: Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

# Exercise 10: Default Dictionary Values
letters_to_numbers = {"a": 1, "b": 2, "c": 3}
print(letters_to_numbers.get("b"))
print(letters_to_numbers.get("d", 0))

# Exercise 11: Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["Eve", 29, "San Francisco"]
person_dict = dict(zip(keys, values))
print(person_dict)

# Exercise 12: Count Occurrences of Words
sentence = "the quick brown fox jumps over the lazy dog the fox"
word_list = sentence.split()
word_count = {word: word_list.count(word) for word in word_list}
print(word_count)
