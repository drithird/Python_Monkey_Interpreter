from abc import ABC, abstractmethod
import monk_int.token.token as token


class Node(ABC):
    @abstractmethod
    def token_literal(self):
        pass


class Statement(Node):
    @abstractmethod
    def statement_node(self):
        pass


class Expression(Node):
    @abstractmethod
    def expression_node(self):
        pass


class Identifier(Node):
    def __init__(self, tok, value):
        self.Token: token.Token = tok
        self.Value: str = value

    def expression_node():
        pass

    def token_literal(self) -> str:
        return self.Token.Literal


class Program(Node):
    def __init__(self):
        self.statements = None

    def token_literal(self):
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""


class LetStatement(Statement):
    def __init__(
        self,
        tok,
    ):
        self.token: token.Token
        self.name: Identifier
        self.value: Expression

    def statement_node(self):
        pass

    def token_literal(self):
        return self.Token.Literal
