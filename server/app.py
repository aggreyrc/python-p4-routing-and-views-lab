#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# @app.route('/print/<string:parameter>')
# def print_string(parameter):
#     return f'<h1>{parameter}</h1>'

@app.route('/print/<string:text>')
def print_text(text):
    print(text)  # This will print to the console
    return text

@app.route('/count/<int:parameter>')
def count(parameter):
    # result = ''
    # for i in range(0, parameter):
    #     result += f'<p>{i}</p>'
    # return result
    return '\n'.join([str(i) for i in range(parameter)]) + '\n'

@app.route('/math/<int:num1>/<path:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation', 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
