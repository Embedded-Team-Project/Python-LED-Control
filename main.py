from flask import Flask, request
import RPi.GPIO as GPIO
import time


app = Flask(__name__)
ledPin = 14

@app.route('/', methods=['GET', 'POST'])
def display_message():
    return hello()

def hello():
    GPIO.setmode(GPIO.BCM)  # setmode를 BCM으로 설정
    GPIO.setup(ledPin, GPIO.OUT)  # 21번핀을 설정

    GPIO.output(ledPin, 1)  # 처음에는 일단 꺼둔 상태
    time.sleep(5)
    GPIO.output(ledPin, 0)  # 처음에는 일단 꺼둔 상태
    return "test";

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

