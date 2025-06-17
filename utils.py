import glob
import json
from datetime import datetime

def print_entries():
    json_files = glob.glob("entries/*.json")

    if not json_files:
        print("   No journal entries are found.")
        return

    json_data = []

    # loads all the json files
    for file in json_files:
        with open(file, "r") as f:
            data = json.load(f)
            data["_filename"] = file
            json_data.append(data)
    
    # sort by most recent first
    json_data.sort(key=lambda e: datetime.strptime(e["date"], "%Y-%m-%d_%H:%M:%S"), reverse=True)

    # format printed entry
    for idx, data in enumerate(json_data, 1):
        tags = ", ".join(data["tags"])
        output_string = f"{idx}. {data['date']} - {data['title']} [{tags}]"

        print(output_string)

print_entries()