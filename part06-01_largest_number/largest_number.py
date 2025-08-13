# write your solution here
def largest():
    max_num = None
    with open("numbers.txt") as file:
        for line in file:
            number = int(line.strip())
            if max_num is None or number > max_num:
                max_num = number
    return max_num

