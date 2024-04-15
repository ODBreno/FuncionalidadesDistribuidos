from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mensagem', methods=['GET'])
def responder_mensagem():
    # Extrai os dados JSON da solicitação
    data = request.json
    
    # Verifica se a chave 'mensagem' está presente nos dados
    if 'mensagem' in data:
        mensagem = data['mensagem']
        resposta = f"A mensagem: {mensagem} foi enviada com sucesso!"
        
        # Retorna a resposta para o barramento
        return jsonify({'resposta': resposta})
    else:
        # Se a chave 'mensagem' não estiver presente, retorna um erro
        return jsonify({'error': 'Nenhuma mensagem enviada, escreva algo!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)