# impersonator-bot

Ensure your terminal has permission to read the iMessages database, chat.db.

Then, you can execute the following commands **from the repo root directory** (impersonator-bot/):

1. `sqlite3 ~/Library/Messages/chat.db ".read [YOUR_ABSOLUTE_PATH_TO_REPO]/impersonator-bot/data_preparation/extract_data.sql" > [YOUR_ABSOLUTE_PATH_TO_REPO]/impersonator-bot/data/raw/output.csv`

    * For example my [YOUR_ABSOLUTE_PATH_TO_REPO] is /Users/yahya/Desktop/code/

2. `python3 ./data_preparation/process_data.py`