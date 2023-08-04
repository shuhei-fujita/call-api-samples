import os
import sys
import json

from git import Repo
from pycodestyle import Checker

sys.path.insert(0, '../gpt')
import get_api_gpt

# リポジトリを開く
repo = Repo('~/git/sample/call-api-samples')

# ブランチを取得
main = repo.heads.main
develop = repo.heads.develop

# 差分を取得
diff_index = main.commit.diff(develop.commit)

# 出力をテキストファイルにリダイレクト
# 出力をテキストファイルにリダイレクト
with open('result.txt', 'w') as f:
    # 差分の各ファイルに対してチェックを行う
    for diff_item in diff_index.iter_change_type('M'):  # 'M'は変更されたファイルを意味します
        # ファイル名を出力
        print(f"Modified file: {diff_item.a_path}", file=f)

path_condition = os.path.join('condition.txt')
path_prompt = os.path.join('result.txt')
responses = get_api_gpt.main(path_condition, path_prompt)
formatted_content=""
for response in responses:
    data = json.loads(response)
    content = data['content']
    formatted_content = content.replace("\\n", "\n")

print(formatted_content)
