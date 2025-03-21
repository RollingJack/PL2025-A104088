from lexer import tokenize


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
        if token is not None and token[0] == 'NUM':
            self.consume()
            return int(token[1])
        raise SyntaxError("Número esperado")

    def term(self):
        result = self.fat()
        while self.current_token() is not None and self.current_token()[0] in ('MULT', 'DIV'):
            op = self.current_token()[0]
            self.consume()
            if op == 'MULT':
                result *= self.fat()
            elif op == 'DIV':
                result //= self.fat()
        return result

    def exp(self):
        result = self.term()
        while self.current_token() is not None and self.current_token()[0] in ('PLUS', 'MINUS'):
            op = self.current_token()[0]
            self.consume()
            if op == 'PLUS':
                result += self.term()
            elif op == 'MINUS':
                result -= self.term()
        return result


if __name__ == "__main__":
    expr = input("Digite a expressão matemática: ")
    tokens = tokenize(expr)
    parser = RecursiveDescentParser(tokens)
    result = parser.exp()
    print(f"{expr} = {result}")
