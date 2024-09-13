#Exercise 8
#8. **Break and Continue**:
#Write a Python program that uses a `while` loop and breaks out of the loop when a certain
#condition is met. Include an option to `continue`, skipping an iteration

n = 5
while n > 0:
    n = n-1
    if n == 2:
        break
    print(n)
print('Loop is finished')