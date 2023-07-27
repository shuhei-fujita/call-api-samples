#!/usr/bin/env python

import openai
from dotenv import load_dotenv
import os
import json
import logging
import time

def main(prompt):
    # ---設定ファイルの初期化---
    path_current = os.path.dirname(os.path.realpath(__file__))

    path_env = os.path.join(path_current, '.env')
    path_prompt = os.path.join(path_current, 'prompt.md')

    load_dotenv(path_env)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    engine_3 = os.getenv('ENGINE_GPT_3')
    engine_4 = os.getenv('ENGINE_GPT_4')

    with open(path_prompt, 'r') as file:
        prompt = file.read()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    # ---設定ファイルの初期化---
    
    # APIリクエスト
    try:
        logging.info('Starting API request...')
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model=engine_3,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        end_time = time.time()
        logging.info('Finished API request in %.2f seconds.', end_time - start_time)
    except Exception as e:
        logging.error('Error occurred during API request: %s', e)
        raise

    # APIレスポンスを整形
    formatted_response = json.dumps(response['choices'][0]['message'], indent=4, ensure_ascii=False)

    # APIレスポンスの実行結果の出力
    with open('result.json', 'w') as json_file:
        json.dump(response['choices'][0]['message'], json_file, indent=4, ensure_ascii=False)
    with open('result.txt', 'w') as txt_file:
        txt_file.write(response['choices'][0]['message']['content'])

    return formatted_response
