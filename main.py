from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/sachin")
def fun1():
    test1 = int(request.args.get('val1'))
    test2 = int(request.args.get('val2'))
    test3 = test1 + test2

    return str(test3)
    # return "<h1> Result is : {}</h1>".format(test3)


if __name__ == '__main__':
    app.run()
