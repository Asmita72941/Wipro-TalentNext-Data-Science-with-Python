#  1. Write a program to print the 4th element from first and 4th element from last in a tuple.

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

fourth_from_start = my_tuple[3]
fourth_from_end = my_tuple[-4]

print("4th element from start:", fourth_from_start)
print("4th element from end:", fourth_from_end)


# 2. Write a program to check whether an element exists in a tuple or not.

my_tuple = (10, 20, 30, 40, 50)
element = 30

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


# 3. Write a program to convert a list into a tuple.

my_list = [10, 20, 30, 40, 50]

my_tuple = tuple(my_list)

print("Original list:", my_list)
print("Converted tuple:", my_tuple)


# 4. Write a program to find the index of an item in a tuple.

my_tuple = (10, 20, 30, 40, 50)

element = 30
if element in my_tuple:
    index = my_tuple.index(element)
    print(f"The index of {element} is {index}.")
else:
    print(f"{element} is not in the tuple.")


# 5. Write a program to replace last value of tuples in a list to 100.  
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

updated_list = [t[:-1] + (100,) for t in sample_list]
print("Updated list:", updated_list)
