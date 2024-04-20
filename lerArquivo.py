from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/lerArquivo', methods=['GET'])
def ler_arquivo():
    data = request.json
    
    if 'cpf' not in data:
        return jsonify({'error': 'Por favor, forneça o cpf!'}), 400
    
    cpf = data['cpf']
    nome_arquivo = f"{cpf}.txt"  # Nome do arquivo a ser lido
    
    # Tenta ler o arquivo e extrair a primeira linha
    try:
        with open(nome_arquivo, 'r') as arquivo:
            saldo = arquivo.readline()
    except Exception as e:
        return jsonify({'mensagem': f'Erro ao ler o arquivo: {str(e)}'}), 500
    
    # Retorna a primeira linha como resposta
    return jsonify({'saldo': saldo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)