from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/through_addressbar")
def fun1():
    test1 = int(request.args.get('val1'))
    test2 = int(request.args.get('val2'))
    test3 = test1 + test2

    return str(test3)
    # return "<h1> Result is : {}</h1>".format(test3)


@app.route("/through_postman", methods=['POST'])
def fun2():
    if (request.method == 'POST'):
        op = request.json['operation']
        n1 = int(request.json['num1'])
        n2 = int(request.json['num2'])

        if (op == 'add'):
            r = n1 + n2
            result = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        if (op == 'sub'):
            r = n1 - n2
            result = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        if (op == 'mul'):
            r = n1 * n2
            result = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        if (op == 'div'):
            r = float(n1) / n2
            result = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        return jsonify(result)

@app.route('/', methods = ['GET',' POST'])
def home():
    return render_template('index.html')

@app.route('/through_html', methods = ['POST'])
def fun3():
    if (request.method == 'POST'):
        op = request.form['operator']
        n1 = int(request.form['number1'])
        n2 = int(request.form['number2'])

        if (op == 'add'):
            r = n1 + n2
            res = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        if (op == 'sub'):
            r = n1 - n2
            res = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        if (op == 'mul'):
            r = n1 * n2
            res = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        if (op == 'div'):
            r = float(n1) / n2
            res = op + " of " + str(n1) + " and " + str(n2) + " is " + str(r)

        return render_template('result.html', result = str(res))


if __name__ == '__main__':
    app.run()
