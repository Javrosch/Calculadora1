from flask import Flask, request, jsonify
import requests
from Algoritmos10 import Catalan, Hanoi, DobFact, Criba, Area_poligono, Armstrong, Esperanza, Determinant_Gauss, FourMeans, Inverse_GaussJordan 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def raiz():
    print("Solicitud recibida en la raíz")
    return "Servidor funcionando"

@app.route('/catalan', methods=['GET'])
def calcular_catalan():
    n = int(request.args.get('n'))
    resultado = Catalan(n)
    return jsonify({'resultado': resultado})

@app.route('/hanoi', methods=['GET'])
def calcular_hanoi():
    n = int(request.args.get('n'))
    resultado = Hanoi(n)
    return jsonify({'resultado': resultado})

@app.route('/dobfact', methods=['GET'])
def calcular_dobfact():
    n = int(request.args.get('n'))
    resultado = DobFact(n)
    return jsonify({'resultado': resultado})

@app.route('/criba', methods=['GET'])
def calcular_criba():
    print("Endpoint /criba llamado")
    n = int(request.args.get('n'))
    resultado = Criba(n)
    print("Resultado:", resultado)
    return jsonify({'resultado': resultado})

@app.route('/', methods=['GET'])
def index():
    return 'Servidor en ejecución'

@app.route('/poligono', methods=['GET'])
def calcular_area_poligono():
    Lado = float(request.args.get('n'))
    NumLados = int(request.args.get('m'))
    resultado = Area_poligono(Lado, NumLados)
    return jsonify({'resultado': resultado})

@app.route('/armstrong', methods=['GET'])
def calcular_armstrong():
    n = int(request.args.get('n'))
    resultado = Armstrong(n)
    return jsonify({'resultado': resultado})

@app.route('/esperanza', methods=['POST'])
def calcular_esperanza():
    datos = request.json
    valores = datos['valores']
    probabilidades = datos['probabilidades']
    if len(valores) != len(probabilidades):
        return jsonify({'error': 'La cantidad de valores y probabilidades no coincide'}), 400
    if abs(sum(probabilidades) - 1) > 0.0001:
        return jsonify({'error': 'La suma de las probabilidades no es igual a 1'}), 400
    esperanza = sum([valor * prob for valor, prob in zip(valores, probabilidades)])
    return jsonify({'esperanza': esperanza})

@app.route('/determinant', methods=['POST'])
def calcular_determinant():
    try:
        data = request.json
        matrix = data['matrix']
        N = len(matrix)
        if not N or not all(len(row) == N for row in matrix):
            return jsonify({'error': 'Matrix must be a non-empty square (N x N).'}), 400

        resultado = Determinant_Gauss(matrix)
        return jsonify({'resultado': resultado})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error during calculation: ' + str(e)}), 500

@app.route('/means', methods=['POST'])
def calcular_means():
    try:
        data = request.json
        if 'data' not in data:
            return jsonify({'error': 'Missing "data" key in request body.'}), 400

        data_list = data['data']
        if not isinstance(data_list, list) or len(data_list) == 0:
            return jsonify({'error': 'Input data must be a non-empty list of numbers.'}), 400

        if not all(isinstance(x, (int, float)) for x in data_list):
            return jsonify({'error': 'All elements in the list must be numbers.'}), 400

        results = FourMeans(data_list)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

print("Definiendo ruta /inverse")
@app.route('/inverse', methods=['POST'])
def calcular_inverse():
    print("Solicitud recibida en /inverse")
    try:
        data = request.json
        print("Datos recibidos:", data)
        matrix = data.get('matrix')
        print("Matriz recibida:", matrix)
        result = Inverse_GaussJordan(matrix)
        print("Resultado:", result)
        return jsonify({'inverse_matrix': result})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500
                        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500)