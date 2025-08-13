# Write your solution here
def histogram(my_string : str):
    words = {}
    for i in my_string:
        if i not in words:
            words[i] = 0
        words[i] += 1
    for key, value in words.items():
        print(f"{key} {value * "*"}")
        
if __name__ == "__main__":
    histogram("statistically")