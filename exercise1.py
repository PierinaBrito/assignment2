#CIS 103: Introduction to Programming
#Lab 02: Python Loops and Object Type
#Description: Homework Assignment / Coding Exercises
#Instructor: Md Ali
#Date: 09/13/2024
#Student: Pierina Brito


#Exercise 1
#1. **While Loop**:
#Write a Python program using a `while` loop that prints numbers from 1 to 10 but exits the
#loop early if the number is greater than 5.


num = 1

while num <= 11:

    if num > 5:
        print("Number is greater than 5, exiting the loop.")
        break

    print(num)

    num += 1
