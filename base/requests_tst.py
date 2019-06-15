import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=dfd1a0f1f6022cd61ee7855bb712ec71&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()
