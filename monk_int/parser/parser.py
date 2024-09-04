import monk_int.ast.ast as ast
import monk_int.lexer.lexer as lexer
import monk_int.token.token as token
from typing import Callable, Dict

prefix_parse = Callable[[], ast.Expression]
infix_parse = Callable[[ast.Expression], ast.Expression]

LOWEST = 1
EQUALS = 2
LESSGREATER = 3
SUM = 4
PRODUCT = 5
PREFIX = 6
CALL = 7


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
        self.errors: [str] = []
        self.prefix_parse_fn: Dict[token.TokenType, prefix_parse] = {}
        self.infix_parse_fn: Dict[token.TokenType, infix_parse] = {}
        self.register_prefix(token.IDENT, self.parse_identifier)
        self.next_token()
        self.next_token()

    def register_prefix(self, token_type: token.TokenType, fn: prefix_parse):
        self.prefix_parse_fn[token_type] = fn
        print(self.prefix_parse_fn.keys())

    def register_infix(self, token_type: token.TokenType, fn: infix_parse):
        self.infix_parse_fn[token_type] = fn

    def Errors(self) -> [str]:
        return self.errors

    def peek_error(self, tok: token.TokenType):
        message = f"expected next token to be {tok}, got {self.peek_token.Type} instead"
        self.errors.append(message)

    def cur_token_is(self, tok: token.TokenType) -> token.TokenType:
        return self.cur_token.Type == tok

    def peek_token_is(self, tok: token.TokenType) -> token.TokenType:
        return self.peek_token.Type == tok

    def expect_peek(self, tok: token.TokenType) -> bool:
        if self.peek_token_is(tok):
            self.next_token()
            return True
        else:
            self.peek_error(tok)
            return False

    def next_token(self):
        """
        This moves the current peek_token to current token and pulls the next token
        """
        self.cur_token = self.peek_token
        self.peek_token = self.lex.NextToken()

    def parse_identifier(self) -> ast.Expression:
        return ast.Identifier(self.cur_token, self.cur_token.Literal)

    def parse_let_statement(self) -> ast.LetStatement:
        statement: ast.LetStatement = ast.LetStatement(tok=self.cur_token)
        if not self.expect_peek(token.IDENT):
            return None
        statement.name = ast.Identifier(self.cur_token, self.cur_token.Literal)
        if not self.expect_peek(token.ASSIGN):
            return None
        # TODO expresions once we begin to handle semicolons
        while not self.cur_token_is(token.SEMICOLON):
            self.next_token()
        return statement

    def parse_return_statement(self) -> ast.ReturnStatement:
        statement: ast.ReturnStatement = ast.ReturnStatement(self.cur_token)
        self.next_token()
        ###TODO Skipping Expresions here as well

        while not self.cur_token_is(token.SEMICOLON):
            self.next_token()

        return statement

    def parse_expression(self, precedence: int) -> ast.Expression:
        prefix = self.prefix_parse_fn.get(self.cur_token.Type)
        if prefix is None:
            return None
        left_expression = prefix()
        return left_expression

    def parse_expression_statement(self) -> ast.ExpressionStatement:
        statement = ast.ExpressionStatement(self.cur_token)
        statement.expression = self.parse_expression(LOWEST)
        if self.peek_token_is(token.SEMICOLON):
            self.next_token()
        return statement

    def parse_statement(self) -> ast.LetStatement:
        match self.cur_token.Type:
            case token.LET:
                return self.parse_let_statement()
            case token.RETURN:
                return self.parse_return_statement()
            case _:
                return self.parse_expression_statement()

    def parse_program(self) -> ast.Program:
        program = ast.Program()
        program.statements = []
        while self.cur_token.Type != token.EOF:
            statement = self.parse_statement()
            if statement is not None:
                program.statements.append(statement)
            self.next_token()
        return program
