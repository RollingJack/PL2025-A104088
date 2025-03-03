import re

TOKEN_TYPES = [
    ('NUM', r'\b\d+\b'),
    ('PA', r'\('),
    ('PF', r'\)'),
    ('DOT',r'\.'),
    ('VIRG', r','),
    ('NEWLINE', r'\n'),
    ('KEYWORD', r'\b(select|where|LIMIT|a)\b'),
    ('VAR', r'\?[a-zA-Z_]\w*'),
    ('IDENTIFIER', r'[a-zA-Z_]+:[a-zA-Z_]+'),
    ('STRING', r'\".*\"'),
    ('LANGTAG', r'@[a-zA-Z]+'),
    ('OP', r'[=:+/]'),
    ('ABRE_CH', r'\{'),
    ('FECHA_CH', r'\}'),
    ('COMMENT', r'\#.*'),
    ('SKIP', r'[ \t]+'),
    ('ERRO', r'.'),
]

MASTER_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

def lexer(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    tokens = []
    for match in re.finditer(MASTER_REGEX, content):
        kind = match.lastgroup
        value = match.group()

        if kind == 'SKIP' or kind == 'COMMENT':
            continue

        if kind == 'ERRO':
            print(f"Erro léxico: '{value}' não reconhecido.")
        
        tokens.append((kind, value))
    return tokens

tokens = lexer('query.txt')

for token in tokens:
    print(token)
