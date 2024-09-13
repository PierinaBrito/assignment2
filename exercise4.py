#Exercise 4

#4. **String Operations**:
#- Write a Python function that takes a string and returns it reversed using slicing.
#- Write a Python function that formats the following output for given variables:
#```
#Name: John, Age: 30, Salary: $50000.50
#```
#Use appropriate field widths to align the output.

def reverse_string(s):
    return s[::-1]  # Slicing to reverse the string

string = "John!"
reversed_string = reverse_string(string)
print(reversed_string)

def format_output(name, age, salary):
    formatted_output = f"Name: {name}, Age: {age}, Salary: ${salary:.2f}"
    print(formatted_output)

name = "John"
age = 30
salary = 50000.50

format_output(name, age, salary)