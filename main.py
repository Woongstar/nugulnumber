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


@app.route('/nugulnumber/plusGame2', methods=['POST'])
def plusGame2():
    response = commonResponse
    plus2_num1 = random.randrange(1, 10)
    plus2_num2 = random.randrange(1, 10)
    plus2_answer = plus2_num1 + plus2_num2
    response['output']['plus2_num1'] = plus2_num1
    response['output']['plus2_num2'] = plus2_num2
    response['output']['plus2_answer'] = plus2_answer

    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/Sum_action', methods=['POST'])
def sumStartAction():
    response = commonResponse
    number1 = random.randrange(1, 5)
    number2 = random.randrange(1, 5)
    answer = number1 + number2
    response['output']['num1'] = number1
    response['output']['num2'] = number2
    response['output']['answer'] = answer

    print(response)
    return json.dumps(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

