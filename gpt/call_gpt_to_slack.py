#!/usr/bin/env python
import os
import sys
import json

sys.path.insert(0, '../gpt')
import call_gpt_api
sys.path.insert(0, '../slack')
import call_slack_api

# ---設定ファイルの初期化---
path_current = os.path.dirname(os.path.realpath(__file__))
path_prompt = os.path.join(path_current, 'prompt.md')
with open(path_prompt, 'r') as file:
    prompt = file.read()

response = call_gpt_api.main(prompt)
data = json.loads(response)
content = data['content']
formatted_content = content.replace("\\n", "\n")

call_slack_api.send_messages(formatted_content)
