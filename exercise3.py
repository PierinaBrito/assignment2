#Exercise 3

#3. **Nested Loop**:
#Write a program to generate the following pattern using nested loops:
#```
#*
#**
#***
#****

# Number of rows for the pattern
rows = 4

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end="")

    print()
