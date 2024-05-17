import os
import shutil


def split_directory(input_directory, percentage):
    # Checking if the input directory exists
    if not os.path.isdir(input_directory):
        raise ValueError(f"The directory {input_directory} does not exist")

    # Creating the output directories
    output_directory = "output_directory"
    percentage_directory = os.path.join(output_directory, str(percentage))
    remaining_percentage = 100 - percentage
    remaining_directory = os.path.join(
        output_directory, str(remaining_percentage))

    os.makedirs(percentage_directory, exist_ok=True)
    os.makedirs(remaining_directory, exist_ok=True)

    # Getting files in the input directory
    files = sorted(os.listdir(input_directory))

    # Calculating the split index
    split_index = int(len(files) * percentage / 100)

    # Splitting the files
    percentage_files = files[:split_index]
    remaining_files = files[split_index:]

    # Coping the files to the output directories
    for file in percentage_files:
        shutil.copy(os.path.join(input_directory, file),
                    os.path.join(percentage_directory, file))

    for file in remaining_files:
        shutil.copy(os.path.join(input_directory, file),
                    os.path.join(remaining_directory, file))

    print(
        f"Files have been split into {percentage}% and {remaining_percentage}% directories.")


# Usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python split_directory.py <input_directory> <percentage>")
    else:
        input_directory = sys.argv[1]
        percentage = int(sys.argv[2])
        split_directory(input_directory, percentage)
