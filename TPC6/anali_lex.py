import ply.lex as lex

tokens = [
    'NUM',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV'
]

t_NUM = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter desconhecido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()