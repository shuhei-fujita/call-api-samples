from git import Repo
from pycodestyle import Checker

# リポジトリを開く
repo = Repo('~/git/sample/call-api-samples')

# ブランチを取得
main = repo.heads.main
develop = repo.heads.develop

# 差分を取得
diff_index = main.commit.diff(develop.commit)

# 差分の各ファイルに対してチェックを行う
for diff_item in diff_index.iter_change_type('M'):  # 'M'は変更されたファイルを意味します
    if diff_item.a_path.endswith('.py'):
        checker = Checker(diff_item.a_path)
        errors = checker.check_all()
        if errors > 0:
            print(f"{errors} errors found in {diff_item.a_path}")
