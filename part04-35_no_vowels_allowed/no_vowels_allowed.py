# Write your solution here
def no_vowels(s):
    vowel = "aeiou"
    return "".join(char for char in s if char not in vowel)

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))