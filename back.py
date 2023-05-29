from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        equation = request.form['equation']
        x0 = float(request.form['x0'])
        tolerance = float(request.form['tolerance'])
        maxIterations = int(request.form['maxIterations'])
    else:
        equation = "x**3 - 2*x**2 - 5"
        x0 = 2
        tolerance = 0.001
        maxIterations = 10

    # Función para evaluar la ecuación en Python
    f = lambda x: eval(equation)

    # Método de Steffensen
    x = x0
    iterations = 0
    data = [{'x': [], 'y': []}]
    errors = []

    while iterations < maxIterations:
        fx = f(x)
        fx_plus_h = f(x + fx)
        x1 = x - (fx**2 / (fx_plus_h - fx))

        data[0]['x'].append(x)
        data[0]['y'].append(fx)
        data[0]['x'].append(x1)
        data[0]['y'].append(f(x1))

        error = abs(x1 - x)
        errors.append(error)

        if error < tolerance:
            break

        x = x1
        iterations += 1

    return render_template('index.html', equation=equation, x0=x0, tolerance=tolerance, maxIterations=maxIterations,
                           iterations=iterations, approximation=x1, func_value=f(x1), errors=errors, data=data)

@app.route('/manual_usuario')
def manual_usuario():
    return render_template('manual_usuario.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')



if __name__ == '__main__':
    app.run(debug=True)
