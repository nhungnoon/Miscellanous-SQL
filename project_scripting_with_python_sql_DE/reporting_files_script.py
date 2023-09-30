import os
import argparse

def search_and_calculate_size(user_path: str, specific_file_type: str):
    # search file ends with specific pattern
    for root, directories, files in os.walk(user_path):
        for _file in files:
            if specific_file_type in _file:
                file_path = os.path.join(root, _file)
                file_size = os.path.getsize(file_path)
                print(f"{file_path} size: {file_size}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user_path", type =str, help="Filepath to find specific files and size")
    parser.add_argument("specific_file_type", type=str, help="Type of files to look for")
    args = parser.parse_args()
    return search_and_calculate_size(args.user_path, args.specific_file_type)

if __name__ == '__main__':
    main()

# Example CLI
# search for file end with .py inside a specific path 
# python3 project_scripting_with_python_sql_DE/reporting_files_script.py project_scripting_with_python_sql_DE .py
