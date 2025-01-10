# turning json into csv

import json
import csv

# Reload paths since the environment has been reset
json_file_path = "/mnt/data/Streaming_History_Audio_2023-2024_5.json"
csv_file_path = "/mnt/data/Spotify_Streaming_History.csv"

# Open the JSON file and parse it
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the desired fields and write to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(["ts", "master_metadata_track_name", "skipped"])
    
    # Write data rows
    for record in data:
        ts = record.get("ts")
        track_name = record.get("master_metadata_track_name", "")
        skipped = record.get("skipped", "")
        csvwriter.writerow([ts, track_name, skipped])

csv_file_path