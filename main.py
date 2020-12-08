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


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/nugulnumber/plusGame2', methods=['POST'])
def plusGame2():
    response = commonResponse
    plus2num1 = random.randrange(1, 6)
    plus2num2 = random.randrange(1, 6)
    plus2num3 = random.randrange(1, 6)
    plus2num4 = random.randrange(1, 6)
    plus2num5 = random.randrange(1, 6)
    plus2num6 = random.randrange(1, 6)
    plus2answer1 = plus2num1 + plus2num2
    plus2answer2 = plus2num3 + plus2num4
    plus2answer3 = plus2num5 + plus2num6
    response['output']['plus2num1'] = plus2num1
    response['output']['plus2num2'] = plus2num2
    response['output']['plus2num3'] = plus2num3
    response['output']['plus2num4'] = plus2num4
    response['output']['plus2num5'] = plus2num5
    response['output']['plus2num6'] = plus2num6
    response['output']['plus2answer1'] = plus2answer1
    response['output']['plus2answer2'] = plus2answer2
    response['output']['plus2answer3'] = plus2answer3

    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/plusGame3', methods=['POST'])
def plusGame3():
    response = commonResponse
    plus3num1 = random.randrange(4, 15)
    plus3num2 = random.randrange(4, 15)
    plus3num3 = random.randrange(4, 15)
    plus3num4 = random.randrange(4, 15)
    plus3num5 = random.randrange(4, 15)
    plus3num6 = random.randrange(4, 15)
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


@app.route('/nugulnumber/plusGame4', methods=['POST'])
def plusGame4():
    response = commonResponse
    plus4num1 = random.randrange(10, 30)
    plus4num2 = random.randrange(10, 30)
    plus4num3 = random.randrange(10, 30)
    plus4num4 = random.randrange(10, 30)
    plus4num5 = random.randrange(10, 30)
    plus4num6 = random.randrange(10, 30)
    plus4answer1 = plus4num1 + plus4num2
    plus4answer2 = plus4num3 + plus4num4
    plus4answer3 = plus4num5 + plus4num6
    response['output']['plus4num1'] = plus4num1
    response['output']['plus4num2'] = plus4num2
    response['output']['plus4num3'] = plus4num3
    response['output']['plus4num4'] = plus4num4
    response['output']['plus4num5'] = plus4num5
    response['output']['plus4num6'] = plus4num6
    response['output']['plus4answer1'] = plus4answer1
    response['output']['plus4answer2'] = plus4answer2
    response['output']['plus4answer3'] = plus4answer3

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

