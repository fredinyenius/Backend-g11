from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicial():
    return {
        'message': 'Bienbenido al api'
    }

@app.route('/', methods=['POST'])
def inicial():
    return {
        'message': 'Bienbenido al api'
    }

if __name__ == '__main__':
    # debug> indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug=True)
