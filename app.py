from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")
@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/triangulo_area',  methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area = n1 * n2 / 2
            return render_template("geometria.html", n1=n1, n2=n2, area=area)

    return render_template("geometria.html")
@app.route('/triangulo_perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro = n1 * 3
            return render_template("geometria.html", n1=n1, perimetro=perimetro)

    return render_template("geometria.html")

@app.route('/circulo_area',  methods=['GET', 'POST'])
def circulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            area1 = 3.14 * (n1 * n1)
            return render_template("geometria.html", n1=n1, area1=area1)

    return render_template("geometria.html")

@app.route('/circulo_perimetro',  methods=['GET', 'POST'])
def circulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            perimetro1 = n1 * 2 * 3.14
            return render_template("geometria.html", n1=n1, perimetro1=perimetro1)

    return render_template("geometria.html")

@app.route('/quadrado_area',  methods=['GET', 'POST'])
def quadrado_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])


            area2 = n1 * n1
            return render_template("geometria.html", n1=n1, area2=area2)

    return render_template("geometria.html")

@app.route('/quadrado_perimetro',  methods=['GET', 'POST'])
def quadrado_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            perimetro2 = n1 * 4
            return render_template("geometria.html", n1=n1, perimetro2=perimetro2)

    return render_template("geometria.html")
@app.route('/hexagono_area',  methods=['GET', 'POST'])
def hexagono_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])


            area3 = (3 * (n1 ** 2) * 1.7) / 2
            return render_template("geometria.html", n1=n1, area2=area3)

    return render_template("geometria.html")

@app.route('/hexagono_perimetro',  methods=['GET', 'POST'])
def hexagono_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            perimetro3 = n1 * 6
            return render_template("geometria.html", n1=n1, perimetro3=perimetro3)

    return render_template("geometria.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)


    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)


    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicacao = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)


    return render_template("operacoes.html")
@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divisao = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)

    return render_template("operacoes.html")



#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)