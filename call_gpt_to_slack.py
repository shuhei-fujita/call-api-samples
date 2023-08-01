import os
import sys
import json

sys.path.insert(0, './gpt')
import get_api_gpt
sys.path.insert(0, './slack')
import get_api_slack
import post_api_slack

# ---設定ファイルの初期化---
path_current = os.path.dirname(os.path.realpath(__file__))

# 1. Slack APIをGETし、チャンネル内のメッセージを取得
# 2. メッセージを、`slack_messages.txt`ファイルに書き込む
get_api_slack.get_messages_in_thread()

# 3. ファイルを読み込んで、GPT-3 に投げる
# 4. GPT-3 の結果をファイルに書き込む
path_prompt = os.path.join(path_current, 'slack_messages.txt')    
responses = get_api_gpt.main(path_prompt)

# 5. ファイルを読み込んで、Slack APIにPOSTする
for response in responses:
    data = json.loads(response)
    content = data['content']
    formatted_content = content.replace("\\n", "\n")
    post_api_slack.send_messages(formatted_content)
