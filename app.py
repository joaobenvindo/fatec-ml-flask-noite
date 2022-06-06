import cloudpickle
from flask import Flask, render_template, request

with open('nbacareer.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Duração de Carreira - NBA')

@app.route('/predicao', methods=['POST'])
def predicao():
  gp = request.form['gp']
  pts = request.form['pts']
  fg = request.form['fg']
  ft = request.form['ft']
  reb = request.form['reb']
  ast = request.form['ast']
  stl = request.form['stl']
  blk = request.form['blk']
  tov = request.form['tov']

  array=[[str(gp), str(pts), str(fg), str(ft), str(reb), str(ast), str(stl), str(blk), str(tov)]]

  predicao = model.predict(array)

  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)
