import json

from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('getip-test.html')


@app.route('/get_ip', methods=['GET', 'POST'])
def get_ip():
    if request.method == 'POST':
        ip = request.form.get('ip')
        print("访问者的IP为：" + str(ip))
        return json.dumps(ip)


if __name__ == '__main__':
    app.run(debug=True, port=5501)
