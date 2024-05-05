import json


# Function to parse the text file and convert it to JSON format
def txt_to_json(file_path):
    data = {}  # Dictionary to store the data

    # Open the text file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines from the file

        statement = None  # Variable to store the current statement

        # Loop through each line in the file
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line:  # Check if the line is not empty
                if line.startswith('"'):  # Check if the line starts with a quote (indicating a new statement)
                    statement = line.strip('"')  # Extract and strip the statement
                    data[statement] = []  # Initialize list for answers and contexts under the current statement
                elif line.startswith(':'):  # Check if the line starts with a colon (indicating an answer and context)
                    parts = line.split(':')  # Split the line by colon ':'
                    answer = parts[1].strip()  # Extract and strip the answer
                    context = parts[2].strip().strip(
                        '"')  # Extract, strip, and remove surrounding quotes from the context
                    data[statement].append({"answer": answer,
                                            "context": context})  # Add answer and context to the list under the current statement

    # Convert the dictionary to JSON format, excluding the "::" signs from the statement keys
    json_data = json.dumps(data, indent=4)
    json_data = json_data.replace(r'\":', '')  # Remove "::" from statement keys

    return json_data


# Path to the text file
file_path = 'big_five_context.txt'

# Transform the text file to JSON format
json_data = txt_to_json(file_path)

# Print the JSON data
print(json_data)


# Function to save JSON data to a file
def save_json(json_data, file_path):
    with open(file_path, 'w') as file:
        file.write(json_data)

# Path to save the JSON file
json_file_path = 'big_five_context.json'

# Save the JSON data to a file
save_json(json_data, json_file_path)

print(f"JSON data saved to '{json_file_path}'")





