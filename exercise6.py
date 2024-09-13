#Exercise 6
#6. **Tuples**:
#Write a Python program that creates a tuple with 5 elements and prints the first and last
#elements. Then, attempt to modify one of the elements and explain the result.


# Create a tuple with 5 elements
my_tuple = (10, 20, 30, 40, 50)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

try:
    my_tuple[1] = 25
except TypeError as e:
    print("Error:", e)
