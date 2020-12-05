# -*-coding:utf-8-*-
from flask import Flask, request, json
from datetime import datetime
import random
import os

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}
}

shoppingItems = [
    ['간장', '2020-09-20'],
    ['설탕', '2020-09-27'],
    ['토마토', '2020-10-10'],
]


def getUtteranceParameter():
    data = request.get_json()
    print('data')
    print(data)
    return data['action']['parameters']


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/createItems', methods=['POST'])
def createItems():
    utteranceParameter = getUtteranceParameter()
    utteranceValue = utteranceParameter['items']['value']

    response = commonResponse

    response['output']['existYn'] = 'N'

    for i in shoppingItems:
        if i[0] == utteranceValue:
            response['output']['existYn'] = 'Y'
            response['output']['registerDate'] = i[1]

    if response['output']['existYn'] == 'N':
        shoppingItems.append([utteranceValue, datetime.today().strftime('%Y-%m-%d')])
    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/Sum_action', methods=['POST'])
def sumStartAction():
    response = commonResponse
    number1 = random.randrange(1, 5)
    number2 = random.randrange(1, 5)

    response['output']['num1'] = number1
    response['output']['num2'] = number2
    response['output']['answer'] = '3'

    print(response)
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

