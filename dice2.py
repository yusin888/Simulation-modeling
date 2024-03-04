import random
from tabulate import tabulate

def map_fraction_to_face(fraction):
    if fraction == "1/6":
        return 1
    elif fraction == "2/6":
        return 2
    elif fraction == "3/6":
        return 3
    elif fraction == "4/6":
        return 4
    elif fraction == "5/6":
        return 5
    elif fraction == "6/6":
        return 6  # Map 6/6 to face 1
    else:
        return None  # Handle other cases if needed

def roll_dice(num_rolls):
    # List of fractions
    fractions = ["1/6", "2/6", "3/6", "4/6", "5/6", "6/6"]

    # Dictionary to store the frequency of each face
    frequency_dict = {fraction: 0 for fraction in fractions}

    # Simulate rolling the dice multiple times
    for _ in range(num_rolls):
        random_fraction = random.choice(fractions)
        frequency_dict[random_fraction] += 1

    # Calculate the percentage for each face
    total_rolls = sum(frequency_dict.values())
    percentage_dict = {fraction: (count / total_rolls) * 100 for fraction, count in frequency_dict.items()}

    # Prepare data for tabular output
    table_data = []
    for fraction in fractions:
        face = map_fraction_to_face(fraction)
        table_data.append([face, frequency_dict[fraction], f"{percentage_dict[fraction]:.2f}%"])

    # Output the results in a table
    headers = ["Face", "Frequency", "Percentage"]
    print("Results of the dice rolls:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Specify the number of rolls
num_rolls = 1000

# Run the dice simulator with the specified number of rolls
roll_dice(num_rolls)
