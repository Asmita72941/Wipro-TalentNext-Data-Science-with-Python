# 1. Write a program to add a key and value to a dictionary.   
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Updated dictionary:", my_dict)


# 2. Write a program to concatenate the following dictionaries to create a new one.  
# Sample Dictionary : 
# dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {}
merged_dict.update(dic1)
merged_dict.update(dic2)
merged_dict.update(dic3)

print("Concatenated dictionary:", merged_dict)


# 3. Write a program to check if a given key already exists in a dictionary.

my_dict = {1: 10, 2: 20, 3: 30}

key_to_check = 2

if key_to_check in my_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")


# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

my_dict = {1: 'Apple', 2: 'Banana', 3: 'Cherry'}

print("Keys:")
for key in my_dict:
    print(key)

print("\nValues:")
for value in my_dict.values():
    print(value)

print("\nKeys and Values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")


# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.

squares_dict = {}

for num in range(1, 16):
    squares_dict[num] = num ** 2

print("Dictionary of squares from 1 to 15:")
print(squares_dict)


# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.

my_dict = {'a': 100, 'b': 200, 'c': 300}

total = sum(my_dict.values())
print("Sum of all values in the dictionary:", total)
