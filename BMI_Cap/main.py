from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    location = request.form['location']
    bmi = weight / (height ** 2)

    return render_template('result.html', bmi=bmi, location=location)

if __name__ == '__main__':
    app.run(debug=True)
