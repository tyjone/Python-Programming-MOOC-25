# Write your solution here
def remove_smallest(numbers: list):
    smallest = min(numbers)        # Find the smallest number
    numbers.remove(smallest)       # Remove it from the original list



if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)