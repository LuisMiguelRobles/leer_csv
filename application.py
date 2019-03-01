from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import csv


app = Flask(__name__)

dataNum = []
pares = []
impares = []



def ca(fileName):
    with open('./'+fileName) as f:

        reader = csv.reader(f)
        """dataNum = list(reader)"""
        global dataNum
        dataNum = [int(item) for sublist in list(reader) for item in sublist]
        
        dataNum.sort()
        for x in dataNum:
            if x % 2 == 0:
                pares.append(x)
            else:
                impares.append(x)



"""def flattener(lst):
    return [int(item) for sublist in lst for item in sublist]"""





@app.route('/')
def index():
    """return render_template('Index.html')"""

    result = dataNum
    return render_template('Index.html', lista=result, pares=pares,impares=impares)


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
            return 'El archivo debe ser .csv'






if __name__ == "__main__":
    app.run()