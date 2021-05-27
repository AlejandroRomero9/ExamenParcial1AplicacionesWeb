from app import app
from flask import render_template
from app.forms import Problema

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def comisiones(comision):
    fijo=5
    if comision < 50000:
        comision= comision + fijo
    elif comision > 50000 and comision <249999:
        comision = comision * 3.65 + 5
    elif comision >250000 and comision < 499999:
        comision = comision * 3.45 + 5
    elif comision >500000 and comision < 999999:
        comision = comision * 3.15 + 5
    elif comision >1000000:
        comision = comision* 2.95 + 5
    return comision
    
    
   

@app.route("/problema", methods=["GET", "POST"])
def problema():
    form=Problema()
    if form.validate_on_submit():
        msj="El calculo neto es: "+str(comisiones(form.honorario.data))
        return render_template("problemaRespuesta.html", form=form,msj=msj)
    return render_template("problema.html", form=form)
