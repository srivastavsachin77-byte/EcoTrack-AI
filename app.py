# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    transport = float(request.form['transport'])
    electricity = float(request.form['electricity'])
    food = float(request.form['food'])
    footprint = transport*0.3 + electricity*0.5 + food*0.2
    return f"Your estimated carbon footprint is {footprint:.2f} kg CO₂/day"

if __name__ == '__main__':
    app.run(debug=True)
