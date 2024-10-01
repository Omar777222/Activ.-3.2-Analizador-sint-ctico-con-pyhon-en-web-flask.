import ply.yacc as yacc
from lexer import tokens

# Definir reglas gramaticales básicas
def p_statement_for(p):
    '''statement : FOR '(' expression ')' '{' expression '}' '''
    p[0] = ('for-loop', p[3], p[6])

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER'''
    p[0] = p[1]

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()
