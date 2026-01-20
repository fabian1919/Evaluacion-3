from flask import Flask, render_template, request


app = Flask(__name__)
app.debug = True
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    r_promedio = None
    r_estado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = "Aprobado" if promedio >=40 and asistencia >= 75 else "Reprobado"

        r_promedio = f"Promedio: {promedio:.2f}"
        r_estado = f"Estado: {estado}"

    return render_template('ejercicio1.html', promedio=r_promedio, estado=r_estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nom_mayor = None
    cant_caract = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        Nombres = [nombre1, nombre2, nombre3]

        nom_mayor = max(Nombres, key=len)
        cant_caract = len(nom_mayor)

    return render_template('ejercicio2.html',nom_mayor=nom_mayor,cant_caract=cant_caract)

if __name__ == '__main__':
    app.run(debug=True)