# Write your solution here
def anagrams(string1 : str,string2 : str):
    if sorted(string1) == sorted(string2):
        return True
    return False

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False

