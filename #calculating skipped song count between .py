#calculating skipped song count between given phase intervals

import json
from datetime import datetime

def load_json_file(file_path):
    """Load the JSON file and return the data."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def count_skipped_entries(data, start_time, end_time):
    """Count the number of entries with 'skipped': true within the given interval."""
    count = 0
    for record in data:
        try:
            ts = datetime.strptime(record["ts"], "%Y-%m-%d %H:%M:%S")
            if start_time <= ts <= end_time and record.get("skipped", False):
                count += 1
        except KeyError:
            continue
        except ValueError:
            continue
    return count

def main():
    """Main function to execute the script."""
    file_path = input("Enter the path to the JSON file: ").strip()
    data = load_json_file(file_path)

    if not data:
        print("Failed to load JSON data.")
        return

    interval_input = input("Enter the timestamp interval (format: YYY-MM-DD HH:MM:SS and YYY-MM-DD HH:MM:SS): ").strip()
    try:
        start_str, end_str = [i.strip() for i in interval_input.split("and")]
        start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid timestamp format. Please use the format: YYY-MM-DD HH:MM:SS and YYY-MM-DD HH:MM:SS")
        return

    count = count_skipped_entries(data, start_time, end_time)
    print(f"Number of 'skipped': true entries in the given interval: {count}")

if __name__ == "__main__":
    main()
