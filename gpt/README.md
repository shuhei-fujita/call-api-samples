# GPT-3 Python Script

- このリポジトリでは、OpenAI の GPT-3 を使用してテキストを生成する Python スクリプトを提供しています。
- スクリプトは、指定されたプロンプトに基づいて GPT-3 からテキストを生成し、結果を標準出力に表示します。

## 前提条件

- Python 3.6 以上がインストールされていること
- OpenAI Python クライアントがインストールされていること
- OpenAI の API キーが取得できること
- .env ファイルに OpenAI の API キーと GPT-3 のモデル名が設定されていること

## インストール

1. `.env` ファイルを定義

```.env
OPENAI_API_KEY=
ENGINE_GPT_3=gpt-3.5-turbo
ENGINE_GPT_4=gpt-4
```

2. スクリプトへのシンボリックリンクを~/bin ディレクトリに作成

```bash
cd ~/bin && \
    ln -s ~/git/tools/call-gpt/script.py call-gpt
```

```bash
cd ~/bin && \
    ln -s ~/git/tools/call-gpt/prompt.md prompt.md
```

3. prompt.md にプロンプトを定義

## # API のレスポンスの実行結果の出力

- result.json
- result.txt

## 参考資料

API Reference

- https://platform.openai.com/docs/api-reference

Daily usage (USD)

- https://platform.openai.com/account/usage

API Keys

- https://platform.openai.com/account/api-keys

Tokenizer

- https://platform.openai.com/tokenizer

ChatGPT の履歴

- https://chat.openai.com/c/d05da0e0-1494-48cb-aaa3-91154a8b5bda
