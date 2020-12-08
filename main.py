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


@app.route('/nugulnumber/multi1', methods=['POST'])
def multi1():
    response = commonResponse
    multi1num1 = random.randrange(1, 4)
    multi1num2 = random.randrange(1, 4)
    multi1num3 = random.randrange(1, 4)
    multi1num4 = random.randrange(1, 4)
    multi1num5 = random.randrange(1, 4)
    multi1num6 = random.randrange(1, 4)
    multi1ans1 = multi1num1 * multi1num2
    multi1ans2 = multi1num3 * multi1num4
    multi1ans3 = multi1num5 * multi1num6

    response['output']['multi1num1'] = multi1num1
    response['output']['multi1num2'] = multi1num2
    response['output']['multi1num3'] = multi1num3
    response['output']['multi1num4'] = multi1num4
    response['output']['multi1num5'] = multi1num5
    response['output']['multi1num6'] = multi1num6
    response['output']['multi1ans1'] = multi1ans1
    response['output']['multi1ans2'] = multi1ans2
    response['output']['multi1ans3'] = multi1ans3

    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/multi2', methods=['POST'])
def multi2():
    response = commonResponse
    multi2num1 = random.randrange(2, 10)
    multi2num2 = random.randrange(2, 10)
    multi2num3 = random.randrange(2, 10)
    multi2num4 = random.randrange(2, 10)
    multi2num5 = random.randrange(2, 10)
    multi2num6 = random.randrange(2, 10)
    multi2ans1 = multi2num1 * multi2num2
    multi2ans2 = multi2num3 * multi2num4
    multi2ans3 = multi2num5 * multi2num6

    response['output']['multi2num1'] = multi2num1
    response['output']['multi2num2'] = multi2num2
    response['output']['multi2num3'] = multi2num3
    response['output']['multi2num4'] = multi2num4
    response['output']['multi2num5'] = multi2num5
    response['output']['multi2num6'] = multi2num6
    response['output']['multi2ans1'] = multi2ans1
    response['output']['multi2ans2'] = multi2ans2
    response['output']['multi2ans3'] = multi2ans3

    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/multi3', methods=['POST'])
def multi3():
    response = commonResponse
    multi3num1 = random.randrange(2, 13)
    multi3num2 = random.randrange(2, 13)
    multi3num3 = random.randrange(2, 13)
    multi3num4 = random.randrange(2, 13)
    multi3num5 = random.randrange(2, 13)
    multi3num6 = random.randrange(2, 13)
    multi3ans1 = multi3num1 * multi3num2
    multi3ans2 = multi3num3 * multi3num4
    multi3ans3 = multi3num5 * multi3num6

    response['output']['multi3num1'] = multi3num1
    response['output']['multi3num2'] = multi3num2
    response['output']['multi3num3'] = multi3num3
    response['output']['multi3num4'] = multi3num4
    response['output']['multi3num5'] = multi3num5
    response['output']['multi3num6'] = multi3num6
    response['output']['multi3ans1'] = multi3ans1
    response['output']['multi3ans2'] = multi3ans2
    response['output']['multi3ans3'] = multi3ans3

    print(response)
    return json.dumps(response)


@app.route('/nugulnumber/challenge1', methods=['POST'])
def challenge1():
    response = commonResponse
    chal1num1 = random.randrange(1, 4)
    chal1num2 = random.randrange(1, 4)
    chal1num3 = random.randrange(1, 4)
    chal1num4 = random.randrange(1, 4)
    chal1num5 = random.randrange(1, 10)
    chal1num6 = random.randrange(1, 10)
    chal1num7 = random.randrange(5, 10)
    chal1num8 = random.randrange(5, 10)
    chal1num9 = random.randrange(5, 25)
    chal1num10 = random.randrange(5, 25)
    chal1num11 = random.randrange(5, 25)
    chal1num12 = random.randrange(5, 30)
    chal1num13 = random.randrange(5, 30)
    chal1num14 = random.randrange(16, 30)
    chal1num15 = random.randrange(16, 30)
    chal1num16 = random.randrange(10, 16)
    chal1ans1 = chal1num1 + chal1num2
    chal1ans2 = chal1num3 + chal1num4
    chal1ans3 = chal1num7 - chal1num2
    chal1ans4 = chal1num1 + chal1num5
    chal1ans5 = chal1num8 - chal1num3
    chal1ans6 = chal1num9 + chal1num6
    chal1ans7 = chal1num10 - chal1num4
    chal1ans8 = chal1num12 + chal1num13
    chal1ans9 = chal1num10 + chal1num3
    chal1ans10 = chal1num15 - chal1num16
    response['output']['chal1num1'] = chal1num1
    response['output']['chal1num2'] = chal1num2
    response['output']['chal1num3'] = chal1num3
    response['output']['chal1num4'] = chal1num4
    response['output']['chal1num5'] = chal1num5
    response['output']['chal1num6'] = chal1num6
    response['output']['chal1num7'] = chal1num7
    response['output']['chal1num8'] = chal1num8
    response['output']['chal1num9'] = chal1num9
    response['output']['chal1num10'] = chal1num10
    response['output']['chal1num11'] = chal1num11
    response['output']['chal1num12'] = chal1num12
    response['output']['chal1num13'] = chal1num13
    response['output']['chal1num14'] = chal1num14
    response['output']['chal1num15'] = chal1num15
    response['output']['chal1num16'] = chal1num16
    response['output']['chal1ans1'] = chal1ans1
    response['output']['chal1ans2'] = chal1ans2
    response['output']['chal1ans3'] = chal1ans3
    response['output']['chal1ans4'] = chal1ans4
    response['output']['chal1ans5'] = chal1ans5
    response['output']['chal1ans6'] = chal1ans6
    response['output']['chal1ans7'] = chal1ans7
    response['output']['chal1ans8'] = chal1ans8
    response['output']['chal1ans9'] = chal1ans9
    response['output']['chal1ans10'] = chal1ans10

    print(response)
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

