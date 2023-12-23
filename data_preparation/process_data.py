import csv
import json
import os

# The Mac from which the data was extracted from may set the handle id to "" and so we need to explicitly replace that
my_handle_id = "+13013662250"
# The handle id for which the bot is trained to impersonate
bot_handle_id = "+13013662250"

csv_file_path = './data/raw/output.csv'
jsonl_file_path = './data/processed/training_data.jsonl'

messages = {}
threads = {}

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for row in csv_reader:
        guid = row["guid"]
        thread_originator_guid = row["thread_originator_guid"]

        if row["id"] != "":
            handle_id = row["id"]
        else:
            handle_id = my_handle_id

        messages[row["guid"]] = {"handle_id":handle_id, "text": row["text"]}

        if thread_originator_guid == None or thread_originator_guid == "":
            continue

        if thread_originator_guid not in threads:
            threads[thread_originator_guid] = [thread_originator_guid]
        else:
            threads[thread_originator_guid].append(guid)

# Define your directories
directory = './data/processed'
if not os.path.exists(directory):
    os.makedirs(directory)
with open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
    for thread_originator_guid in threads:
        if thread_originator_guid not in messages:
            continue
        
        current_input_text = "%s: %s" % (messages[thread_originator_guid]["handle_id"], messages[thread_originator_guid]["text"])

        for i in range(1, len(threads[thread_originator_guid])):
            message = messages[threads[thread_originator_guid][i]]

            if message["handle_id"] == bot_handle_id and not message["text"].startswith("Liked") and not message["text"].startswith("Disliked") and not message["text"].startswith("Loved") and not message["text"].startswith("Laughed at") and not message["text"].startswith("Emphasized") and not message["text"].startswith("Questioned"):
                row = {
                    "input_text": current_input_text,
                    "output_text": "%s: %s" % (bot_handle_id, message["text"])
                }
                jsonl_file.write(json.dumps(row) + '\n')
            
            current_input_text += ", %s: %s" % (message["handle_id"], message["text"])