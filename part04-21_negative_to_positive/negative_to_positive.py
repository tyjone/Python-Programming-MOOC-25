# Write your solution here
# Ask the user for a positive integer
N = int(input("Enter a positive integer: "))

# Ensure the input is positive
for i in range(-N, N + 1):
    if i != 0:
        print(i)
