# Write your solution here
def formatted(numbers):
    return [f"{num:.2f}" for num in numbers]

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)