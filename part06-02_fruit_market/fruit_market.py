# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.strip()  # Remove newline and extra spaces
            if ";" in line:
                name, price = line.split(";")
                fruits[name] = float(price)
    return fruits

print(read_fruits())