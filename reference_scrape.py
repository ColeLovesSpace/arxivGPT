# your_script.py
import sys

def process_file(file_path):
    # Your file processing logic here
    with open(file_path, 'r') as file:
        content = file.read()
        processed_data = content.upper()  # Example: Convert text to uppercase

    return processed_data

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    result = process_file(input_file_path)
    print(result)
