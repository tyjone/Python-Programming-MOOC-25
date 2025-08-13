# Write your solution here
def filter_solutions():
    correct_lines = []
    incorrect_lines = []

    with open('solutions.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) != 3:
                continue  # skip malformed lines

            name, problem, result_str = parts
            try:
                expected = eval(problem)
                given = int(result_str)
                if expected == given:
                    correct_lines.append(line)
                else:
                    incorrect_lines.append(line)
            except Exception:
                incorrect_lines.append(line)

    # Write results
    with open('correct.csv', 'w') as correct_file:
        correct_file.writelines(correct_lines)

    with open('incorrect.csv', 'w') as incorrect_file:
        incorrect_file.writelines(incorrect_lines)
