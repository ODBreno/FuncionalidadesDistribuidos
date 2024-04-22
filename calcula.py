from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular', methods=['GET'])
def calcular():
    # Extrai os dados JSON da solicitação
    data = request.json
    print(data)
    # Verifica se todas as chaves necessárias estão presentes nos dados
    if 'numero1' not in data or 'operador' not in data or 'numero2' not in data:
        return jsonify({'error': 'Por favor, forneça número 1, operador e número 2!'}), 400
    
    # Extrai os números e o operador
    print(data)
    numero1 = data['numero1']
    operador = data['operador']
    numero2 = data['numero2']
    
    # Realiza a operação matemática com base no operador
    if operador == '+':
        resultado = numero1 + numero2
        print(resultado)
    elif operador == '-':
        resultado = numero1 - numero2
        print(resultado)
    elif operador == '*':
        resultado = numero1 * numero2
        print(resultado)
    elif operador == '/':
        if numero2 == 0:
            return jsonify({'resultado': 'Não é possível dividir por zero!'}), 400
        resultado = numero1 / numero2
    else:
        return jsonify({'resultado': f'O operador {operador} não é suportado!'}), 400
    
    # Retorna o resultado da operação
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
