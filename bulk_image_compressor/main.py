import os
from PIL import Image

# I wouldn't usually add this here but this code is for a friend so I'm trying
# to make it easier to use.
feedback = False


def compress_images(input_directory, quality, feedback):
    # Ensure the input directory exists
    if not os.path.isdir(input_directory):
        raise ValueError(f"The directory {input_directory} does not exist")

    # Define the output directory
    output_directory = "output_directory"

    # Check if the output directory already exists
    if os.path.exists(output_directory):
        print(
            f"The directory {output_directory} already exists. Please move or rename it.")
        exit(1)

    # Create the output directory
    os.makedirs(output_directory, exist_ok=True)

    # Get list of files in the input directory
    files = os.listdir(input_directory)

    for file in files:
        file_path = os.path.join(input_directory, file)

        # Check if the file is an image
        try:
            with Image.open(file_path) as img:
                output_file_path = os.path.join(output_directory, file)
                img.save(output_file_path, optimize=True, quality=quality)

                if feedback:
                    print(f"Compressed {file} and saved to {output_file_path}")

        except (IOError, SyntaxError) as e:
            print(f"Skipping file {file}, as it is not a valid image.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python compress_images.py <input_directory> <quality>")
    else:
        input_directory = sys.argv[1]
        quality = int(sys.argv[2])
        compress_images(input_directory, quality, feedback)
