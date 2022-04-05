import requests

def lambda_handler(event, context):
    res = requests.get("http://www.yahoo.co.jp/")
    return res.status_code