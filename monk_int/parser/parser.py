import monk_int.ast.ast as ast
import monk_int.lexer.lexer as lexer


class Parser:
    def __init__(self, lex: lexer.Lexer):
        self.lex = lex
        self.cur_token = None
        self.peek_token = None

        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lex.NextToken()

    def parse_program(self):
        return ast.Program()
