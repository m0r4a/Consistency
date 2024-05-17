import os
import shutil


def get_next_output_directory(base_name, percentage):
    i = 2
    remaining_percentage = 100 - percentage

    if os.path.exists(f"{base_name}_{percentage}_{remaining_percentage}"):
        while os.path.exists(f"{base_name}_{percentage}_{remaining_percentage}_{i}"):
            i += 1
        return f"{base_name}_{percentage}_{remaining_percentage}_{i}"

    else:
        return f"{base_name}_{percentage}_{remaining_percentage}"


def split_directory(input_directory, percentage):
    # Check if the input directory exists
    if not os.path.isdir(input_directory):
        raise ValueError(f"The directory {input_directory} does not exist")

    # Create the next available output directory
    output_directory = get_next_output_directory(
        "output_directory", percentage)
    percentage_directory = os.path.join(output_directory, str(percentage))
    remaining_percentage = 100 - percentage
    remaining_directory = os.path.join(
        output_directory, str(remaining_percentage))

    # For 50% split, create directories with _1 and _2 suffix
    if percentage == 50:
        percentage_directory += "_1"
        remaining_directory += "_2"

    os.makedirs(percentage_directory, exist_ok=True)
    os.makedirs(remaining_directory, exist_ok=True)

    # Get list of files in the input directory
    files = sorted(os.listdir(input_directory))

    # Calculate the split index
    split_index = int(len(files) * percentage / 100)

    # Split the files
    percentage_files = files[:split_index]
    remaining_files = files[split_index:]

    # Copy the files to the respective directories
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
