import glob
import json
from datetime import datetime

# print entries in the entries folder
def load_entries():
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
    return json_data

def print_entries():
    json_data = load_entries()
    print("\nJournal Entries:\n")
    # format printed entry
    for idx, data in enumerate(json_data, 1):
        tags = ", ".join(data["tags"])
        output_string = f"{idx}. {data['date']} - {data['title']} [{tags}]"

        print(output_string)
    
    return json_data

# view entries
def view_entries():
    json_data = print_entries()
    user_input = input("\nView entry by entry number or title: ").strip()
    single_entry = None
    # entry number
    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(json_data):
            single_entry = json_data[index]
        else:
            print("   Invalid entry number.")
            return
    # title matching
    else:
        all_matches = []
        for entry in json_data:
            if (user_input.lower() in entry["title"].lower()):
                all_matches.append(entry)
        if len(all_matches) == 0:
            print("   No matching entry title found.")
            return
        elif len(all_matches) > 1:
            print("   Multiple matches found. Try to be more specific.")
            for entry in all_matches:
                print(f" - {entry['title']} ({entry['date']})")
            return
        else:
            single_entry = all_matches[0]

    # all printing of entry
    print("\nEntry Details\n" + "-" * 40)
    print(f"Title: {single_entry['title']}")
    print(f"Date: {single_entry['date']}")
    print(f"Tags: {', '.join(single_entry['tags'])}")
    print("\nContent:\n" + single_entry['content'])
    print("-" * 40)
view_entries()