from datetime import datetime
import os
import json
import re

# cleaning string file for saving in directory
def slugify(title: str, max_length: int = 50):
    title = title.lower().replace("’", "").replace("'", "")
    slug = re.sub(r'[^a-z0-9]+', '-', title)
    stopwords = {'a', 'an', 'and', 'on', 'the', 'of', 'in', 'for', 'to', 'with'}
    words = [word for word in slug.split('-') if word and word not in stopwords]
    cleaned_slug = '-'.join(words)[:max_length]
    final_slug = re.sub(r'-{2,}', '-', cleaned_slug).strip('-')
    return final_slug

def create_entry():
    title = input("Add a name for your journal entry: ").strip()
    while (title == ""):
        print("   Title can't be empty. Enter a valid title.")
        title = input("Add a name for your journal entry: ").strip()

    print("Enter your content here. Create an empty line once you are finished: ")
    all_content = ""
    content = input()
    while (content != ""):
        all_content += content + "\n"
        content = input()
    
    tags = input("Enter tags with commas (e.g. \"ai, moods, happiness\"): ")

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")

    save_entry(title, all_content, tags, formatted_datetime)

def save_entry(title, content, tags, timestamp):
    filename = f"{timestamp}_{slugify(title)}.json"
    entry = {
        "title": title,
        "date": timestamp,
        "tags": [t.strip() for t in tags.split(",")],
        "content": content.strip()
    }

    os.makedirs("entries", exist_ok=True)
    filepath = os.path.join("entries", filename)

    with open(filepath, "w") as f:
        json.dump(entry, f, indent = 4)
    
    print(f"\n Entry saved as {filename}")

create_entry()