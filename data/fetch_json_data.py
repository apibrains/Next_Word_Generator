import json
import pandas as pd

data = json.load(open('./data\EmailSum_data.json'))

# Accessing all content
all_content = []

# Iterate over each thread
for thread in data["data"]["train"]:
    # Add short summary content
    short_summary = thread["short_summary"]["content"]
    all_content.append(short_summary.strip())
    
    # Add long summary content
    long_summary = thread["long_summary"]["content"]
    all_content.append(long_summary.strip())
    # print(thread)

# Print all content

df = pd.DataFrame({"sentence": all_content})

old_csv = pd.read_csv('./data\data.csv')

new_csv = pd.concat([old_csv, df])

new_csv.to_csv('./data\data.csv', index=False)

