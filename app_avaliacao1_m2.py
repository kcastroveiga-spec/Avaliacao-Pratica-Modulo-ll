from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/soma")
def somar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    soma = valor1 + valor2
    return jsonify({"resutado": soma})

@app.route("/subtrair")
def subtrair():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    subtrair = valor1 - valor2
    return jsonify({"resutado": subtrair})

@app.route("/multiplicar")
def multiplicar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    multiplicar = valor1 * valor2
    return jsonify({"resutado": multiplicar})

@app.route("/dividir")
def dividir():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    dividir = valor1 / valor2
    return jsonify({"resutado": dividir})

if __name__ == "__main__":

    app.run(debug=True)
