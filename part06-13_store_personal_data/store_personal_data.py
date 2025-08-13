# Write your solution here
def store_personal_data(person: tuple):
    name, age, height = person
    line = f"{name};{age};{height}\n"
    
    with open("people.csv", "a", encoding="utf-8") as file:
        file.write(line)

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))

