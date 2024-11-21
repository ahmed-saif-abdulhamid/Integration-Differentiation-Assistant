from flask import Flask, request, jsonify, render_template
from sympy import symbols, integrate, latex
from sympy.parsing.latex import parse_latex

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    latex_expression = data.get('expression', '')
    variable = data.get('variable', 'x')

    try:
        x = symbols(variable)
        expression = parse_latex(latex_expression)
        result = integrate(expression, x)
        latex_result = latex(result)  
        return jsonify({'result': latex_result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
