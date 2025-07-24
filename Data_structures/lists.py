# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.

list_items = [1, 2, 3, 4, 5]
for i in range(len(list_items)):
    print(f"Element at index {i}: {list_items[i]}")


# 2. Write a program to append a new item to the end of the list.

list_items.append(10)
print(f"List after appending a new item: {list_items}")


# 3. Write a program to reverse the order of the items in the list.

print("Original list:", list_items)
list_items.reverse()
print("Reversed list:", list_items)


# 4. Write a program to print the number of occurrences of a specified element in a list.

numbers = [10, 20, 30, 20, 40, 50, 20]
print("List:", numbers)
element = 20
count = numbers.count(element)

print(f"The number {element} occurs {count} times in the list.")


# 5. Write a program to append the items of list1 to list2 in the front.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("List1:", list1)
print("List2:", list2)

list2 = list1 + list2
print("Updated List2 after adding List1 to the front:", list2)


# 6. Write a program to insert a new item before the second element in an existing list.

numbers = [10, 20, 30, 40]
print("Original list:", numbers)

new_item = 15
numbers.insert(1, new_item)

print("Updated list:", numbers)


# 7. Write a program to remove the item from a specified index in a list.

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

index_to_remove = 2

if 0 <= index_to_remove < len(numbers):
    removed_item = numbers.pop(index_to_remove)
    print(f"Item {removed_item} removed from index {index_to_remove}")
else:
    print("Invalid index!")


# 8. Write a program to remove the first occurrence of a specified element from a list.

numbers = [10, 20, 30, 20, 40, 50]
print("Original list:", numbers)

element_to_remove = 20

if element_to_remove in numbers:
    numbers.remove(element_to_remove)
    print(f"First occurrence of {element_to_remove} removed.")
else:
    print(f"{element_to_remove} not found in the list.")

print("Updated list:", numbers)
