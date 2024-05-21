import subprocess
import json
import sys

def run_cloudsplaining_scan(input_file, output_directory):
    command = [
        "cloudsplaining",
        "scan",
        "--input-file",
        input_file,
        "--output",
        output_directory
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Cloudsplaining scan: {e}")

if __name__ == "__main__":
    # Provided JSON string
    
    json_string = sys.stdin.read()
    # Clean the string
    
    cleaned_json_string = json_string.replace("\\r", "").replace("\\n", "").replace("    ", "")
    
    # Convert cleaned JSON string to dictionary
    data = json.loads(cleaned_json_string)
    # Write the data to a JSON file
    with open("example.json", "w") as file:
        json.dump(data, file)

    input_file = "example.json"  # Replace with your input JSON file path
    output_directory = "output/"  # Replace with your output directory path
    run_cloudsplaining_scan(input_file, output_directory)
    


