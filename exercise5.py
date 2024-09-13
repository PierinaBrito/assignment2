
# 5. **List Operations**:
# - Create a list of integers. Write Python code to:
# - Append a number to the list.
# - Insert a number at a specific index.
# - Sort the list in ascending order.
# - Pop the last element of the list and print it.
# - Remove a specific number from the list.


# Create a list of integers
my_list = [5, 3, 8, 1, 9]

# Append a number to the list
my_list.append(7)
print("After appending:", my_list)

# Insert a number at a specific index (e.g., insert 4 at index 2)
my_list.insert(2, 4)
print("After inserting at index 2:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Pop the last element of the list and print it
last_element = my_list.pop()
print("Popped element:", last_element)
print("After popping:", my_list)

# Remove a specific number from the list (e.g., remove 3)
my_list.remove(3)
print("After removing 3:", my_list)
