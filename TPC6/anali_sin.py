import re

class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def consume(self):
        self.pos += 1
    
    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return None
    
    def fat(self):
        token = self.current_token()
        if token is not None and token.isdigit():
            self.consume()
            return int(token)
        raise SyntaxError("Número esperado")
    
    def term(self):
        result = self.fat()
        while self.current_token() in ('*', '/'):
            op = self.current_token()
            self.consume()
            if op == '*':
                result *= self.fat()
            elif op == '/':
                result //= self.fat()
        return result
    
    def exp(self):
        result = self.term()
        while self.current_token() in ('+', '-'):
            op = self.current_token()
            self.consume()
            if op == '+':
                result += self.term()
            elif op == '-':
                result -= self.term()
        return result

def tokenize(expr):
    return re.findall(r'\d+|[+\-*/]', expr)



expr = input("Digite a expressão matemática: ")

tokens = tokenize(expr)
parser = RecursiveDescentParser(tokens)
result = parser.exp()
print(f"{expr} = {result}")