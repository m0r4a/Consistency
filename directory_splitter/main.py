import os
import shutil
import sys


def get_next_output_directory(base_name, percentage):
    # Calculating and defining variables
    i = 2
    remaining_percentage = 100 - percentage

    # Defining the output directory names
    first_output_directory = f"{base_name}_{percentage}_{remaining_percentage}"
    second_or_more_output_directory = f"{base_name}_{percentage}_{remaining_percentage}_{i}"

    # Check if the first output directory exists and if it does
    # check for the next available output directory

    if os.path.exists(first_output_directory):
        while os.path.exists(second_or_more_output_directory):
            i += 1
        return second_or_more_output_directory
    else:
        return first_output_directory


def split_directory(input_directory, percentage):
    # Check if the input directory exists
    if not os.path.isdir(input_directory):
        raise ValueError(f"The directory {input_directory} does not exist")

    # Create the next available output directory name
    output_directory = get_next_output_directory(
        "output_directory", percentage)

    # Creating the output directories paths
    percentage_directory = os.path.join(output_directory, str(percentage))
    remaining_percentage = 100 - percentage
    remaining_directory = os.path.join(
        output_directory, str(remaining_percentage))

    # Managing the special case of 50% split
    if percentage == 50:
        percentage_directory += "_1"
        remaining_directory += "_2"

    # Actually creating the directories
    os.makedirs(percentage_directory, exist_ok=True)
    os.makedirs(remaining_directory, exist_ok=True)

    # Getting the list of files in the input directory and sorting them
    files = sorted(os.listdir(input_directory))

    # Calculating the split index
    split_index = int(len(files) * percentage / 100)

    # Splitting the files
    percentage_files = files[:split_index]
    remaining_files = files[split_index:]

    # Now im copying the files to the output directories
    for file in percentage_files:
        shutil.copy(os.path.join(input_directory, file),
                    os.path.join(percentage_directory, file))

    for file in remaining_files:
        shutil.copy(os.path.join(input_directory, file),
                    os.path.join(remaining_directory, file))

    print(
        f"Files have been split into {percentage}% and {remaining_percentage}% directories.")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python split_directory.py <input_directory> <percentage>")

    else:
        input_directory = sys.argv[1]
        percentage = int(sys.argv[2])
        split_directory(input_directory, percentage)
