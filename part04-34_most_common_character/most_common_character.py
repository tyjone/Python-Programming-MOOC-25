# Write your solution here
def most_common_character(s):
    return max(s, key = lambda c : s.count(c))

if __name__ == "__main__":
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))