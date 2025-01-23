from telethon import TelegramClient, events
import asyncio
import time
import random

class Colors:
    GREEN = "\033[92m"  
    RED = "\033[91m"    
    RESET = "\033[0m"   

accounts = [
    {"session": "account1", "api_id": {api_id}, "api_hash": "{api_hash}",
     "phone_number": "{phone_number}"},
]

excluded_user_ids = {user_id, user_id_2}

messages = [
    "Hi its me again.",
]

delay = 60
sent_users = set()

def select_account():
    print("Hesaplar:")
    for i, account in enumerate(accounts):
        print(f"{i} - {account['phone_number']}")

    account_index = int(input("Select account ? (Number): "))
    return accounts[account_index]

async def add_members_to_group(client, group):
    try:
        members = await client.get_participants(group)
        print(f"Gruptaki {len(members)} üye alındı.")
        await client.add_participants(group, members)
        print(f"{len(members)} user added back to the group.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

async def main():
    selected_account = select_account()

    client = TelegramClient(selected_account["session"],
                            selected_account["api_id"],
                            selected_account["api_hash"])

    async with client:
        await client.start(phone=selected_account["phone_number"])
        print(f"{selected_account['phone_number']} ile giriş yapıldı!")

        groups = []
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                groups.append(dialog)

        print("Gruplar:")
        for i, group in enumerate(groups):
            print(f"{i} - {group.title}")
        group_index = int(input("Selecet group ? (Number): "))
        target_group = groups[group_index]
        print(f"Seçilen grup: {target_group.title}")

        add_to_group = input("Can u add this group user ? (0(no)/1(yes)): ").strip().lower()
        if add_to_group == '1':
            await add_members_to_group(client, target_group)
        else:
            print("User not add group.")

        try:
            members = await client.get_participants(target_group)
            print(f"{len(members)} User finded.")
            if len(members) < 5:
                print("This group is hidden, messages will be sent to the message senders.")
                await listen_to_messages(client, target_group)
            else:
                print("Users Listed...")
                for member in members:
                    if member.id not in sent_users and member.id not in excluded_user_ids:
                        try:
                            message = random.choice(messages)
                            print(f"Sending Message: {member.id}")
                            await client.send_message(member.id, message)
                            sent_users.add(member.id)
                            print(f"{Colors.GREEN}Message Success Sending: {member.id}{Colors.RESET}")
                            time.sleep(delay)
                        except Exception as e:
                            print(f"{Colors.RED}Err: {e}{Colors.RESET}")
                    else:
                        print(f"Not Send Message : {member.id} (Excluded user)")
        except Exception as e:
            print(f"Hidden group detected. Focusing on message senders. Error: {e}")
            await listen_to_messages(client, target_group)

async def listen_to_messages(client, target_group):
    print("Tracking those who send messages...")

    @client.on(events.NewMessage(chats=target_group))
    async def handler(event):
        if event.is_private:
            sender = await event.get_sender()
            message_content = event.message.message
            print(f"{sender.id} received private message from user: {message_content}")

            if sender.id not in sent_users and sender.id not in excluded_user_ids:
                try:
                    message = random.choice(messages)
                    print(f"Message Sending: {sender.id}")
                    await client.send_message(sender.id, message)
                    sent_users.add(sender.id)
                    print(f"{Colors.GREEN}Message Success Send: {sender.id}{Colors.RESET}")
                except Exception as e:
                    print(f"{Colors.RED}Err: {e}{Colors.RESET}")
            else:
                print(f"{Colors.RED}Message Failed: {sender.id} (Excluded user){Colors.RESET}")
        else:
            sender = await event.get_sender()
            message_content = event.message.message
            print(f"{sender.id} received a group message from the user: {message_content}")

    print("Those who send messages are listened to...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
