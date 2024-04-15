from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alterarArquivo', methods=['GET'])
def alterar_arquivo():
    # Extrai os dados JSON da solicitação
    data = request.json
    print(data)
    # Verifica se todas as chaves necessárias estão presentes nos dados
    if 'nome_arquivo' not in data or 'texto' not in data:
        return jsonify({'mensagem': 'Por favor, forneça o nome do arquivo e o texto!'}), 400
    
    # Extrai o nome do arquivo e o texto
    nome_arquivo = data['nome_arquivo']
    texto = data['texto']
    
    # Tenta criar ou alterar o arquivo com o texto fornecido
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto)
    except Exception as e:
        return jsonify({'mensagem': f'Erro ao criar ou alterar o arquivo: {str(e)}'}), 500
    
    # Retorna uma mensagem de sucesso
    return jsonify({'mensagem': f'O arquivo {nome_arquivo} foi criado ou alterado com sucesso!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)