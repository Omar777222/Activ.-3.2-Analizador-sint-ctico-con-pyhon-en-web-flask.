from flask import Flask, request, render_template
from lexer import lexer  # Importar el analizador léxico
from parser import parser  # Importar el analizador sintáctico

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    token_results = []
    parse_status = "Esperando análisis..."

    if request.method == 'POST':
        # Leer el archivo o el código ingresado
        file = request.files.get('file')
        if file:
            text = file.read().decode('utf-8')
        else:
            text = request.form.get('code', '')

        # Realizar el análisis léxico
        lexer.input(text)
        for tok in lexer:
            token_results.append({
                'line': tok.lineno,
                'type': tok.type,
                'value': tok.value,
                'correct_structure': 'X' if tok.type == 'FOR' else '',
                'incorrect_structure': 'X' if tok.type != 'FOR' else ''
            })

        # Realizar el análisis sintáctico
        try:
            parser.parse(text)
            parse_status = "El análisis sintáctico se realizó correctamente."
        except Exception as e:
            parse_status = f"Error en el análisis sintáctico: {str(e)}"

    return render_template('index.html', results=token_results, parse_status=parse_status)

if __name__ == '__main__':
    app.run(debug=True)
