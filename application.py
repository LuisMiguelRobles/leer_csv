from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import csv
from flask_bootstrap import Bootstrap
import re
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
# Expresion regular para verificar numeros
regex = re.compile(r'[0-9]+')

numeros = []
pares = []
impares = []


def ca(file_name):
    with open(os.path.join('./uploads/', file_name)) as f:
        reader = csv.reader(f, delimiter=',')

        global numeros
        global pares
        global impares
        pares = []
        impares = []
        numeros = [float(item) for sublist in list(reader) for item in sublist if regex.search(item)]
        numeros.sort()
        pares_impares(numeros, pares, impares)
        """for x in numeros:

            if x % 2 == 0:
                pares.append(x)
            else:
                impares.append(x)"""


@app.route('/')
def index():
    limpiar()
    return render_template('Index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    global fileName
    if request.method == 'POST':
        f = request.files['file']
        if f.filename.endswith('.csv'):

            f.save(os.path.join('./uploads/', secure_filename(f.filename)))
            ca(f.filename)
            return render_template('Data.html', data=numeros, pares=pares, impares=impares)
        else:
            return render_template('Error.html')


def pares_impares(lst, lst_par, lst_impar):
    for x in lst:
        if x % 2 == 0:
            lst_par.append(x)
        else:
            lst_impar.append(x)


def limpiar():
    pares.clear()
    impares.clear()


if __name__ == "__main__":
    app.run()
