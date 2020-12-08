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




def getUtteranceParameter():
    data = request.get_json()
    print('data')
    print(data)
    return data['action']['parameters']


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/nugulnumber/numberbaseball', methods=['POST'])
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


@app.route('/nugulnumber/plusGame3', methods=['POST'])
def plusGame3():
    response = commonResponse
    plus3num1 = random.randrange(10, 20)
    plus3num2 = random.randrange(10, 20)
    plus3num3 = random.randrange(10, 20)
    plus3num4 = random.randrange(10, 20)
    plus3num5 = random.randrange(10, 20)
    plus3num6 = random.randrange(10, 20)
    plus3answer1 = plus3num1 + plus3num2
    plus3answer2 = plus3num3 + plus3num4
    plus3answer3 = plus3num5 + plus3num6
    response['output']['plus3num1'] = plus3num1
    response['output']['plus3num2'] = plus3num2
    response['output']['plus3num3'] = plus3num3
    response['output']['plus3num4'] = plus3num4
    response['output']['plus3num5'] = plus3num5
    response['output']['plus3num6'] = plus3num6
    response['output']['plus3answer1'] = plus3answer1
    response['output']['plus3answer2'] = plus3answer2
    response['output']['plus3answer3'] = plus3answer3

    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/multipleGame', methods=['POST'])
def multiple():
    response = commonResponse
    multiplenumber1 = random.randint(1, 10)
    multiplenumber2 = random.randint(1, 10)
    multipleanswer = multiplenumber1 * multiplenumber2
    response['output']['multiplenumber1'] = multiplenumber1
    response['output']['multiplenumber2'] = multiplenumber2
    response['output']['multipleanswer'] = multipleanswer

    print(response)
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

