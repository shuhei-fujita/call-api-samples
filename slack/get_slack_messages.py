import os
from dotenv import load_dotenv
from slack_sdk import WebClient
import datetime

load_dotenv()
slack_token = os.environ['SLACK_API_TOKEN']
slack_channel_id = os.environ['SLACK_CHANNEL_ID']
client = WebClient(token=slack_token)

# 上限あり
def get_messages_in_thread():
    # Slackのチャンネル内のメッセージ履歴をすべて取得
    response_conversations = client.conversations_history(
        channel=slack_channel_id,
        limit=100
    )
    with open('slack_messages.txt', 'w') as f:
        for message in response_conversations.data['messages']:
            f.write(f"{message['text']}\n")
        
        dt_now = datetime.datetime.now()
        f.write(f"{dt_now}\n")

# 上限なし
def get_messages_in_thread_no_limit():
    all_messages = []
    response = client.conversations_history(
        channel=slack_channel_id,
        limit=1000
    )
    all_messages.extend(response['messages'])

    # Check if more messages are available
    while response['has_more']:
        # Get the cursor for the next page of messages
        cursor = response['response_metadata']['next_cursor']

        # Get the next page of messages
        response = client.conversations_history(
            channel=slack_channel_id,
            cursor=cursor,
            limit=1000
        )
        all_messages.extend(response['messages'])

    with open('slack_messages.txt', 'w') as f:
        for message in all_messages:
            f.write(f"{message['text']}\n")
        
        dt_now = datetime.datetime.now()
        f.write(f"{dt_now}\n")

if __name__ == "__main__":
    # get_messages_in_thread()
    get_messages_in_thread_no_limit()
