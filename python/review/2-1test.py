from flask import Flask,request,jsonify

app= Flask(__name__)
@app.route('/door',methods=['GET'])
def door():
    p =request.args.get("p")
    if p=="open":
        return jsonify(code=0,msg="开门")
    elif p == 'close':
        return jsonify(code=1,msg="关门")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')