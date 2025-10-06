from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/soma")
def somar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    soma = valor1 + valor2
    return jsonify({"resutado": soma})

@app.route("/subtrai")
def subtrair():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    subtrai = valor1 - valor2
    return jsonify({"resutado": subitrai})

if __name__ == "__main__":
    app.run(debug=True)