import monk_int.ast.ast as ast
import monk_int.lexer.lexer as lexer
import monk_int.token.token as token


class Parser:
    def __init__(self, lex: lexer.Lexer):
        """
        This class creates a Parser object that will allow you to parse all the code

        input:
        lex: lexer.Lexer : A lexer object that has been created on the code input

        output:
        Parser
        """
        self.lex = lex
        self.cur_token = None
        self.peek_token = None

        self.next_token()
        self.next_token()

    def cur_token_is(self, tok: token.TokenType):
        return self.cur_token.Type == tok

    def peek_token_is(self, tok: token.TokenType):
        return self.peek_token.Type == tok

    def expect_peek(self, tok: token.TokenType):
        if self.peek_token_is(tok):
            self.next_token()
            return True
        else:
            return False

    def parse_let_statement(self):
        statement: ast.LetStatement = ast.LetStatement(tok=self.cur_token)
        if not self.expect_peek(token.IDENT):
            return None
        statement.Name = ast.Identifier(self.cur_token, self.cur_token.Literal)
        if not self.expect_peek(token.ASSIGN):
            return None
        # TODO expresions once we begin to handle semicolons
        while not self.cur_token_is(token.SEMICOLON):
            self.next_token()

    def next_token(self):
        """
        This moves the current peek_token to current token and pulls the next token
        """
        self.cur_token = self.peek_token
        self.peek_token = self.lex.NextToken()

    def parse_statement(self):
        match self.cur_token.Type:
            case token.LET:
                return self.parse_let_statement()

    def parse_program(self):
        program = ast.Program()
        program.statements = []
        count = 0
        while self.cur_token.Type != token.EOF:
            statement = self.parse_statement()
            if statement is not None:
                program.statements.append(statement)
            self.next_token()
        return program
