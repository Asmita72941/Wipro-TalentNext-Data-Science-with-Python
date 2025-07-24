# 1. Write a program to remove a given item from the set.

my_set = {10, 20, 30, 40, 50}

item_to_remove = 30
my_set.discard(item_to_remove)

print("Updated set after removing", item_to_remove, ":", my_set)


# 2. Write a program to create an intersection of sets.

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)


# 3. Write a program to create an union of sets.

set1 = {10, 20, 30}
set2 = {30, 40, 50}

union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)


# 4. Write a program to find the maximum and minimum value in a set.

numbers = {10, 50, 30, 70, 20}

max_value = max(numbers)
min_value = min(numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
