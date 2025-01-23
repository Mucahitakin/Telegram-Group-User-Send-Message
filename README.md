# Telegram Message Sender Bot

## Overview

This Telegram bot is designed to send messages to users in a selected group. It utilizes the Telethon library to interact with the Telegram API, allowing for automated messaging based on specific criteria. The bot can also add users back to a group and listen for incoming messages from users.

## Features

- **Account Selection**: Users can select from multiple Telegram accounts to operate the bot.
- **Group Management**: The bot can add users back to a specified group.
- **Message Sending**: Sends random messages from a predefined list to users in the selected group, excluding certain users.
- **Message Listening**: Listens for incoming messages from users and responds accordingly.

## Requirements

- Python 3.7 or higher
- Telethon library
- Telegram API credentials (API ID and API Hash)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

   ```bash
   pip install telethon
   ```

3. Replace the placeholders in the `accounts` list with your actual Telegram API credentials:

   ```python
   accounts = [
       {"session": "account1", "api_id": {api_id}, "api_hash": "{api_hash}",
        "phone_number": "{phone_number}"},
   ]
   ```

4. Update the `excluded_user_ids` set with the user IDs you want to exclude from messaging.

5. Modify the `messages` list to include the messages you want the bot to send.

## Usage

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. Follow the prompts to select an account and a group.

3. Decide whether to add users back to the group.

4. The bot will then send messages to users in the selected group, excluding any specified in the `excluded_user_ids` set.

5. If the group is hidden, the bot will listen for incoming messages from users and respond with a random message from the list.

## Code Explanation

- **Colors Class**: Contains ANSI escape codes for coloring console output.
- **select_account()**: Prompts the user to select a Telegram account.
- **add_members_to_group()**: Adds users back to the specified group.
- **main()**: The main function that orchestrates the bot's operations, including selecting a group and sending messages.
- **listen_to_messages()**: Listens for incoming messages from users and responds with a random message.

## Notes

- Ensure that the bot has the necessary permissions to send messages and add users to groups.
- Be mindful of Telegram's terms of service regarding automated messaging to avoid being banned.
