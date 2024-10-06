import json

def read_values_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()  # Read the entire file as a single string

    # Split the data into parts using commas
    values = [value.strip() for value in data.split(',') if value.strip()]  # Remove whitespace and empty strings

    # Initialize lists to hold x and y values
    x_values = []
    y_values = []

    # Loop through the values
    for clean_value in values:
        if clean_value:  # Proceed only if there's something to convert
            # Check for brackets in the x values
            if clean_value.startswith("(") and clean_value.endswith(")"):
                # Temporarily store x value as a string and convert to float
                x_string = clean_value[1:-1]  # Remove the brackets
                try:
                    # Convert to complex and append the real part to x_values
                    x_value = complex(x_string).real  # Get only the real part
                    x_values.append(x_value)
                except ValueError:
                    print(f"Skipping malformed x value: '{clean_value}'")  # Debug output
            else:
                # Append y values directly (assuming they are already in proper float format)
                try:
                    y_values.append(float(clean_value))
                except ValueError:
                    print(f"Skipping malformed y value: '{clean_value}'")  # Debug output

    return x_values, y_values

def create_dict(x_values, y_values):
    return dict(zip(x_values, y_values))

def write_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    input_filename = 'values.txt'  # Name of the input file
    x_values, y_values = read_values_from_file(input_filename)
    
    # Check if lengths match
    if len(x_values) != len(y_values):
        print("Error: The lengths of x and y values do not match. Exiting program.")
        return

    # Create the dictionary and write to JSON
    paired_data = create_dict(x_values, y_values)
    write_to_json(paired_data, 'coords.json')
    print("Data has been written to coords.json successfully.")

if __name__ == '__main__':
    main()
