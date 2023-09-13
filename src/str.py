import random
import string

def add_random_string(file_path, length):
    # Generate a random string for the file name
    random_file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    # Find the position of the last dot in the file path
    last_dot_index = file_path.rfind('.')

    if last_dot_index != -1:
        # Split the file path into base and extension
        base = file_path[:last_dot_index]
        extension = file_path[last_dot_index:]

        # Construct the new file path with the random string
        new_file_path = f"{base}_{random_file_name}{extension}"
    else:
        # If no dot is found in the path, simply append the random string to the end
        new_file_path = f"{file_path}_{random_file_name}"

    return new_file_path