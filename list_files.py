"""
AI File Manager - File Listing Utility

This module provides functionality to recursively scan directories and generate
a list of all file paths within the specified directory structure.
"""

import os
import argparse

def list_files(directory: str, output_file: str, encoding: str = 'utf-8') -> None:
    """
    Recursively list all files in a directory and write their paths to an output file.
    
    This function walks through the specified directory and all its subdirectories,
    collecting the full path of every file found and writing each path on a separate
    line to the output file.
    
    Args:
        directory (str): The path to the directory to scan. Can be an absolute or
                        relative path.
        output_file (str): The path to the output file where file paths will be written.
                          If the file exists, it will be overwritten.
        encoding (str, optional): Text encoding for the output file. Defaults to 'utf-8'.
    
    Returns:
        None
    
    Raises:
        Exception: If there's an error accessing the directory or writing to the output file.
                  The specific error message will be printed to the console.
    
    Example:
        >>> list_files("/home/user/documents", "file_list.txt")
        File paths have been written to file_list.txt
    """
    try:
        with open(output_file, 'w', encoding=encoding) as f:
            for root, _, files in os.walk(directory):
                for file in files:
                    # Write the full path of each file
                    file_path = os.path.join(root, file)
                    f.write(file_path + '\n')
        print(f"File paths have been written to {output_file}")
    except (OSError, IOError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recursively scan a directory and list all file paths to an output file."
    )

    parser.add_argument(
        "--directory",
        help="Directory to scan for files (can be absolute or relative path)"
    )

    parser.add_argument(
        "--output_file", 
        default="temp/file_list.txt",
        help="Output file to write the list of file paths to"
    )

    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Text encoding for the output file (default: utf-8)"
    )

    args = parser.parse_args()

    list_files(args.directory, args.output_file, args.encoding)
