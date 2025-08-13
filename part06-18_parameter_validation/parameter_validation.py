# Write your solution here
def new_person(name: str, age: int):
    # Strip whitespace and validate name
    if not name or len(name.strip().split()) < 2 or len(name) > 40:
        raise ValueError("Invalid name: must be at least two words, non-empty, and no more than 40 characters.")
    
    # Validate age
    if age < 0 or age > 150:
        raise ValueError("Invalid age: must be between 0 and 150.")

    return (name, age)
