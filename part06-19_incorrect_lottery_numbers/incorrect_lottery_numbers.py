# Write your solution here
def filter_incorrect():
    def is_valid_line(header, numbers):
        # Validate header format: should be "week X" where X is a positive integer
        if not header.startswith("week "):
            return False
        try:
            week_num = int(header[5:])
            if week_num < 1:
                return False
        except ValueError:
            return False

        # Validate we have exactly 7 numbers
        if len(numbers) != 7:
            return False

        seen = set()
        for num_str in numbers:
            try:
                num = int(num_str)
            except ValueError:
                return False
            if not (1 <= num <= 39):
                return False
            if num in seen:
                return False
            seen.add(num)

        return True

    with open("lottery_numbers.csv", "r") as infile, open("correct_numbers.csv", "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) != 2:
                continue

            header = parts[0]
            numbers = parts[1].split(",")

            if is_valid_line(header, numbers):
                outfile.write(line + "\n")
