from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import csv
from flask_bootstrap import Bootstrap
import numbers
import re


app = Flask(__name__)
bootstrap = Bootstrap(app)

regex = re.compile(r'[0-9]+')
"""regex = re.compile(r'[^.0-9][0-9]+')"""
dataNum = []
datos=[]
pares = []
impares = []


def ca(fileName):
    with open('./'+fileName) as f:

        reader = csv.reader(f, delimiter=';')
        """dataNum = list(reader)"""
        global dataNum
        dataNum = [int(item) for sublist in list(reader) for item in sublist if regex.search(item)]
        dataNum.sort()
        print(dataNum)
        for x in dataNum:
            print(type(x))
            if x % 2 == 0:
                pares.append(x)
            else:
                impares.append(x)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    global fileName
    if request.method == 'POST':
        f = request.files['file']
        if f.filename.endswith('.csv'):

            f.save(secure_filename(f.filename))
            ca(f.filename)
            """return 'file uploaded successfully'"""
            return render_template('Data.html', data=dataNum, pares=pares, impares=impares)
        else:
            return render_template('Error.html')








if __name__ == "__main__":
    app.run()