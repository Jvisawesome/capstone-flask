
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'nombre_app': 'CapstoneApp',
        'version': '1.0',
        'autor': 'Tu Nombre'
    })

@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    respuesta = f"Recibido: {mensaje}"
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)
