# AWS Bedrock環境のLLMを提供するのAPIを使用するPythonスクリプトを提供します
from dotenv import load_dotenv
import sys, os
module_path = "../utils"
sys.path.append(os.path.abspath(module_path))
import bedrock as util_w

load_dotenv()

os.environ['LANGCHAIN_ASSUME_ROLE'] = '<YOUR_VALUES>'
boto3_bedrock = util_w.get_bedrock_client(os.environ['LANGCHAIN_ASSUME_ROLE'])

bedrock = boto3.client(service_name='bedrock',
region_name='us-east-1',
endpoint_url='https://bedrock.us-east-1.amazonaws.com')

response = bedrock.invoke_model(
    body={
        "inputText": "this is where you place your input text",
        "textGenerationConfig": {
            "maxTokenCount": 4096,
            "stopSequences": [],
            "temperature":0,
            "topP":1
        },
    },
    modelId="amazon.titan-tg1-large", 
    accept=accept, 
    contentType=contentType)

print(response['payload'].read())

def call_llm_api():
    # レスポンスを確認
    if response.status_code == 200:
        # 成功した場合、結果を返す
        return response.json()
    else:
        # エラーがあった場合、エラーメッセージを返す
        return response.text

if __name__ == "__main__":
    call_llm_api()
