import os
import logging
import requests
import json

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
slack_token = os.environ['SLACK_API_TOKEN']
channel_id = os.environ['SLACK_CHANNEL_ID']
webhook_url = os.environ['SLACK_WEBHOOK_URL']
client = WebClient(token=slack_token)

# Slack Botでメッセージを送信する
# requests.post(webhook_url, data=json.dumps({
#     "text" : "Hello World",
# }))

# Slack APIのWebClientでメッセージを送信する
try:
    response = client.chat_postMessage(
        channel=channel_id, 
        text="Hello world"
    )
    logging.info(response)

except SlackApiError as e:
    logging.error(f"Error posting message: {e}")
