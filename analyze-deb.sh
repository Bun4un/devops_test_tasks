#!/bin/bash

# Check if a .deb file path is provided as an argument
if [ -z "$1" ]; then
    echo "Error: Please provide the path to the .deb file"
    exit 1
fi

DEB_FILE="$1"

# Check if the file exists
if [ ! -f "$DEB_FILE" ]; then
    echo "Error: File $DEB_FILE not found"
    exit 1
fi

# Extract the package name and dependencies
PACKAGE_NAME=$(dpkg-deb -f "$DEB_FILE" Package)
DEPENDENCIES=$(dpkg-deb -f "$DEB_FILE" Depends)

# Output the results
echo "Package Name: $PACKAGE_NAME"
echo "Dependencies:"
echo "$DEPENDENCIES" | tr ',' '\n'  # Display each dependency on a new line
