#!/bin/bash

# Prompt the user for a folder path
read -p "Enter the folder path: " folder_path

# Check if the folder already exists
if [ -d "$folder_path" ]; then
 echo "Folder already exists."
else
 # If the folder doesn't exist, create it
 mkdir -p "$folder_path"

 # Move into the new folder
 cd "$folder_path"

 # Download and install a package (e.g., 'example_package' for demonstration)
 wget https://example.com/example_package.tar.gz
 tar -xzf example_package.tar.gz

 # You can add installation steps here if necessary

 echo "Folder created and package downloaded."
fi