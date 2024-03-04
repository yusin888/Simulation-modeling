import random
from tabulate import tabulate

def map_fraction_to_face(fraction):
    if 0 <= fraction < 1/6:
        return 1
    elif 1/6 <= fraction < 2/6:
        return 2
    elif 2/6 <fraction < 3/6:
        return 3
    elif 3/6 <= fraction < 4/6:
        return 4
    elif 4/6 <= fraction < 5/6:
        return 5
    elif 5/6 <= fraction < 1:
        return 6  # Map 6/6 to face 1
    else:
        return None  # Handle other cases if needed

def roll_dice(num_rolls):
    # Dictionary to store the frequency of each face
    frequency_dict = {i+1: 0 for i in range(6)}

    # Simulate rolling the dice multiple times
    for _ in range(num_rolls):
        random_fraction = random.random()
        face = map_fraction_to_face(random_fraction)
        frequency_dict[face] += 1

    # Calculate the percentage for each face
    total_rolls = sum(frequency_dict.values())
    percentage_dict = {face: (count / total_rolls) * 100 for face, count in frequency_dict.items()}

    # Prepare data for tabular output
    table_data = [[face, frequency_dict[face], f"{percentage_dict[face]:.2f}%"] for face in range(1, 7)]

    # Output the results in a table
    headers = ["Face", "Frequency", "Percentage"]
    print("Results of the dice rolls:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Specify the number of rolls
num_rolls = 1000

# Run the dice simulator with the specified number of rolls
roll_dice(num_rolls)
