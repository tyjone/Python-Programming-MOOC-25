# Write your solution here
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    result = {}

    for i in range(100):
        if i < 10:
            result[i] = ones[i]
        elif 10 <= i < 20:
            result[i] = teens[i - 10]
        else:
            tens_place = i // 10
            ones_place = i % 10
            if ones_place == 0:
                result[i] = tens[tens_place]
            else:
                result[i] = f"{tens[tens_place]}-{ones[ones_place]}"

    return result

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
        