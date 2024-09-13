#Exercise 7
#7. **Dictionary Operations**:
#- Create a dictionary with the following key-value pairs: `{'name': 'John', 'age': 25, 'city':
#'New York'}`.
#- Write Python code to:
#- Add a new key-value pair to the dictionary.
#- Update the value of the `age` key.
#- Remove the `city` key from the dictionary.
#- Print all the keys and values in the dictionary.

# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Add a new key-value
my_dict['salary'] = 50000
print("After adding 'salary':", my_dict)

# Update the value of the 'age' key
my_dict['age'] = 30
print("After updating 'age':", my_dict)

# Remove the 'city' key
my_dict.pop('city')
print("After removing 'city':", my_dict)

# Print all the keys and values
print("Keys and values in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
