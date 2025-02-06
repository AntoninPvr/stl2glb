#!/bin/bash

# Function to duplicate a file
duplicate_file() {
    local num_copies="$1"
    local file_path="$2"
    local destination_dir="$3"

    # Check if the file exists
    if [ ! -f "$file_path" ]; then
        echo "The file $file_path does not exist."
        return 1
    fi

    # Create the destination directory if it doesn't exist
    mkdir -p "$destination_dir"

    # Loop to create multiple copies
    for i in $(seq 1 "$num_copies"); do
        # Create new file name
        new_file_path="$destination_dir/"$i"_$(basename "$file_path")"
        
        # Copy the file
        cp "$file_path" "$new_file_path"
        echo "Copied $file_path to $new_file_path"
    done
}

# Check if the correct number of arguments is passed
if [ $# -ne 3 ]; then
    echo "Usage: $0 <file_path> <num_copies> <destination_dir>"
    exit 1
fi

# Get input arguments
num_copies="$1"
file_path="$2"
destination_dir="$3"

# Call the function with the input arguments
duplicate_file "$num_copies" "$file_path" "$destination_dir"
