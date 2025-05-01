from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao Projeto CI/CD com Jenkins! Nova atualização!!'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)