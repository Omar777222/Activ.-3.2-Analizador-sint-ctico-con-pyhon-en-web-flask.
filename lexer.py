import ply.lex as lex

# Definición de tokens
tokens = ['FOR', 'WHILE', 'IF', 'ELSE', 'IDENTIFIER', 'NUMBER']

# Definición de palabras reservadas
reserved = {
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE'
}

# Expresiones regulares para tokens simples
t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verificar si es una palabra reservada
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
