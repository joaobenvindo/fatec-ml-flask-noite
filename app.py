from flask import Flask, render_template, request
import cloudpickle

# with open('model.pkl', 'rb') as file_in:
#  model_loaded = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicao', methods=["POST"])    
def predicao():
    nome = request.form['firstname']
    predicao = model.predict(['firstname'])
    return str(predicao[0])

app.run(debug=True)
