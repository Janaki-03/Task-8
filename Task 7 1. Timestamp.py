import datetime

def create_text_file_with_timestamp():
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Create a file with the timestamp as the filename
    file_name = f"file_{timestamp_str}.txt"

    # Write the timestamp as content to the file
    with open(file_name, "w") as file:
        file.write(f"Timestamp: {timestamp_str}\n")

    print(f"Text file '{file_name}' created with the current timestamp as content.")

# Call the function to create the text file
create_text_file_with_timestamp()