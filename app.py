from flask import Flask, flash, render_template, url_for, request, redirect
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario
from sqlalchemy import select
from flask_login import LOGIN_MESSAGE, login_user, logout_user, current_user, LoginManager, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENAI_SP'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Para visualizar essa pagina faça o login'


@app.route("/")
def home():
    return render_template("home.html")


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')

        # Se campos vazios
        if not email or not senha:
            flash('Preencher todos os campos!', 'danger')
            return render_template("login.html")

        verificar_email = select(Funcionario).where(Funcionario.email == email)
        resultado_email = db_session.execute(verificar_email).scalar_one_or_none()

        # Usuário não existe
        if resultado_email is None:
            flash('Funcionário não encontrado!', 'danger')
            return render_template("login.html")

        # Senha errada
        if not resultado_email.check_password(senha):
            flash('Senha incorreta!', 'danger')
            return render_template("login.html")

        # Login correto
        login_user(resultado_email)
        flash('Login efetuado com sucesso!', 'success')
        return redirect(url_for('home'))

    # GET sempre retorna
    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout efetuado com sucesso!', 'success')
    return redirect(url_for('login'))




@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form_nome')
        data_nascimeto = request.form.get('form_data')
        cpf = request.form.get('form_cpf')
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        cargo = request.form.get('form_cargo')
        salario = request.form.get('form_salario')
        if not nome or not email or not senha:
            flash('Preencher todos os campos!', 'danger')
            return render_template('cadastro.html')
        verificar_email = select(Funcionario).where(Funcionario.email == email)
        existe_email = db_session.execute(verificar_email).scalar_one_or_none()
        verificar_cpf = select(Funcionario).where(Funcionario.cpf == cpf)
        existe_cpf = db_session.execute(verificar_cpf).scalar_one_or_none()
        if existe_email:
            flash(f'Email {email} ja está cadastrado!', 'danger')
            return render_template('cadastro.html')
        if existe_cpf:
            flash(f'CPF {cpf} ja está cadastrado!', 'danger')
            return render_template('cadastro.html')
        try:
            novo_funcionario = Funcionario(nome=nome, data_nascimeto=data_nascimeto, cpf=cpf, cargo=cargo,
                                           salario=salario, email=email)
            novo_funcionario.set_password(senha)
            db_session.add(novo_funcionario)
            db_session.commit()
            flash(f'Usuario {nome} cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar funcionário!', 'danger')
            print(f'Erro na base de dados:{e}')
            return redirect(url_for('cadastro_funcionario'))
        except Exception as e:
            flash(f'Erro as cadastrar Funcionário!', 'danger')
            print(f'Erro ao cadastrar:{e}')
            return redirect(url_for('cadastro_funcionario'))
    return render_template('cadastro.html')


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/funcionarios')
@login_required
def funcionarios():
    func_sql = select(Funcionario)
    resultado = db_session.execute(func_sql).scalars().all()
    return render_template("funcionarios.html", resultado=resultado)



@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/triangulo_area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area = n1 * n2 / 2
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, n2=n2, area=area)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a area do triangulo", 'alert-danger')

    return render_template("geometria.html")


@app.route('/triangulo_perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro = n1 * 3
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro=perimetro)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a area do triangulo", 'alert-danger')

    return render_template("geometria.html")


@app.route('/circulo_area', methods=['GET', 'POST'])
def circulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            area1 = 3.14 * (n1 * n1)
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, area1=area1)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a area do circulo", 'alert-danger')

    return render_template("geometria.html")


@app.route('/circulo_perimetro', methods=['GET', 'POST'])
def circulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            perimetro1 = n1 * 2 * 3.14
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro1=perimetro1)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar o perimetro do circulo", 'alert-danger')

    return render_template("geometria.html")


@app.route('/quadrado_area', methods=['GET', 'POST'])
def quadrado_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            area2 = n1 * n1
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, area2=area2)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a area do quadrado", 'alert-danger')

    return render_template("geometria.html")


@app.route('/quadrado_perimetro', methods=['GET', 'POST'])
def quadrado_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            perimetro2 = n1 * 4
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro2=perimetro2)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar o perimetro do quadrado", 'alert-danger')

    return render_template("geometria.html")


@app.route('/hexagono_area', methods=['GET', 'POST'])
def hexagono_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            area3 = (3 * (n1 ** 2) * 1.7) / 2
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, area2=area3)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a area do hexagono", 'alert-danger')

    return render_template("geometria.html")


@app.route('/hexagono_perimetro', methods=['GET', 'POST'])
def hexagono_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])

            perimetro3 = n1 * 6
            flash("Calculo realisado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro3=perimetro3)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar o perimetro do hexagono", 'alert-danger')

    return render_template("geometria.html")


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Soma realisada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)

        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            flash("Subtração realisada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)

        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a subtração", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicacao = n1 * n2
            flash("Multiplicaçaõ realisada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)
        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a multiplicação", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divisao = n1 / n2
            flash("Divisão realisada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)

        else:
            # Passo-1: Emitir a mensagem e categoria falsh
            flash("Preencha o campo para realizar a divisão", 'alert-danger')

    return render_template("operacoes.html")


# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)
