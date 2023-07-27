import os
import logging

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
slack_token = os.environ['SLACK_API_TOKEN']
slack_channel_id = os.environ['SLACK_CHANNEL_ID']
slack_thread_url = os.environ['SLACK_THREAD_URL']
slack_thread_id = ""
client = WebClient(token=slack_token)

def send_messages(send_text):
    # Slack APIのWebClientでメッセージを送信する
    try:
        response = client.chat_postMessage(
            channel=slack_channel_id, 
            text=send_text
        )
        logging.info(response)

    except SlackApiError as e:
        logging.error(f"Error posting message: {e}")

def get_messages_in_thread():
    parts = slack_thread_url.split("/p")
    slack_thread_id_with_dot = parts[-1]
    thread_ts = f"{slack_thread_id_with_dot[:10]}.{slack_thread_id_with_dot[10:]}"

    # Slackのスレッド内のメッセージを取得
    try:
        response_conversations = client.conversations_replies(
            channel=slack_channel_id,
            ts=thread_ts
        )
        print(response_conversations["messages"])
        message_list = [msg['text'] for msg in response_conversations["messages"] if 'text' in msg]
        formatted_messages = "\n".join(message_list)

        # フォーマットを出力
        output_format = f"""
スレッドのメッセージリスト:

{formatted_messages}

SLACK_slack_thread_id={thread_ts}
https://shuhei-fujita.slack.com/archives/C05JMARDS8P/p{slack_thread_id}
        """

    except SlackApiError as e:
        logging.error(f"Error retrieving thread messages: {e}")

    # Slack APIのWebClientでメッセージを送信する
    send_messages(output_format)

if __name__ == "__main__":
    get_messages_in_thread()
    # send_messages('sample')
