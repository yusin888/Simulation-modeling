import random
from tabulate import tabulate

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
        table_data.append([fraction, frequency_dict[fraction], f"{percentage_dict[fraction]:.2f}%"])

    # Output the results in a table
    headers = ["Fraction", "Frequency", "Percentage"]
    print("Results of the dice rolls:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Specify the number of rolls
num_rolls = 1000

# Run the dice simulator with the specified number of rolls
roll_dice(num_rolls)
