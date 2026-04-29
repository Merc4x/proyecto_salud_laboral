from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', active_page='inicio')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', active_page='nosotros')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', active_page='servicios')

@app.route('/capacitaciones')
def capacitaciones():
    return render_template('capacitaciones.html', active_page='capacitaciones')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
