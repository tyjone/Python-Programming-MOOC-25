# Write your solution here
limit = int(input("Limit: "))
result = 0
i = 1
message = "The consecutive sum: "
while i <= limit:

    if result < limit:
        message += str(i)
        result += i
    i += 1
    if result < limit:
        message += " + "

message += f" = {result}"

print(message)