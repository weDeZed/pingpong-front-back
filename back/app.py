from flask import Flask
from flask_cors import CORS
from joueur import joueur_bp



app = Flask(__name__)
app.register_blueprint(joueur_bp)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
