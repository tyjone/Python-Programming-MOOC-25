# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list = [x,y,z]
    return (min(list),max(list),sum(list))

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))