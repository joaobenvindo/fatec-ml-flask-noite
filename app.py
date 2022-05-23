from flask import Flask, render_template, request
import cloudpickle

# with open('model.pkl', 'rb') as file_in:
#  model_loaded = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicao', methods=['POST'])
def predicao():
  PD = request.form['Partidas Disputadas']
  predicao = model.predict([PD])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)
