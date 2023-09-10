def read_text_file(file_name):
    try:
        # Open the file for reading
        with open(file_name, "r") as file:
            # Read and display the content
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_name = "Task 1.txt"  # Replace with the actual file name
read_text_file(file_name)