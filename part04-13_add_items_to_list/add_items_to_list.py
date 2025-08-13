# Write your solution here
items_amount = int(input("How many items: "))
n = 0
n += items_amount
i = 1
item = []
while n > 0:
    item.append(int(input(f"Item {i}: ")))
    i += 1
    n -= 1
print(item)