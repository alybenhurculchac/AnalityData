from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)
@app.route('/')
def ontology_page():
    html  = """<html><body>"""
    html += """<h2>Consultas disponibles</h2>""" 
  #  html += """<h2>'%s' ontology</h2>""" % onto.base_iri
  #  html += """<h3>Root classes</h3>"""
  #  for Class in Thing.subclasses():
  #      html += """<p>>%s</p>""" % Class.name
   #     html += """<p>>%s</p>""" % len(g)
   
    
    html += """<div>
                <p>Seleccione su consulta:</p>
  <form action="/result">
    <input type="radio" id="1" name="c" value="1">
  <label for="1">Consulta 1</label><br>
  <input type="radio" id="2" name="c" value="2">
  <label for="2">Consulta 2</label><br>
  <input type="radio" id="3" name="c" value="3">
  <label for="3">Consulta 3 Saludos hola</label>
  </p>
<p><input type="submit"></p>
    </form>
    </div>""" 
    
    return html

port=os.environ["PORT"]
app.run('0.0.0.0',port, debug=True)

