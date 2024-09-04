from abc import ABC, abstractmethod
import monk_int.token.token as token


class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

    def __str__(self) -> str:
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
        self.token: token.Token = tok
        self.value: str = value

    def expression_node():
        pass

    def token_literal(self) -> str:
        return self.token.Literal

    def __str__(self):
        return str(self.value)


class Program(Node):
    def __init__(self):
        self.statements = None

    def token_literal(self):
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""

    def __str__(self):
        out = []
        for s in self.statements:
            out.append(str(s))  # Assuming each statement has a __str__ method
        return "".join(out)


class LetStatement(Statement):
    def __init__(
        self,
        tok,
    ):
        self.token: token.Token = tok
        self.name: Identifier
        self.value: Expression

    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.Literal

    def __str__(self):
        out = []
        out.append(self.token_literal() + " ")
        out.append(str(self.name.token_literal()))
        out.append(" = ")
        if self.value is not None:
            out.append(str(self.value.token_literal()))

        out.append(";")
        return "".join(out)


class ReturnStatement(Statement):
    def __init__(self, tok):
        self.token: token.Token = tok
        self.return_value: Expression

    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.Literal

    def __str__(self):
        out = []
        out.append(self.token_literal() + " ")
        if self.return_value is not None:
            out.append(str(self.return_value))
        out.append(";")
        return "".join(out)


class ExpressionStatement(Statement):
    def __init__(self, tok):
        self.token: token.Token
        self.expression: Expression

    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.Literal

    def __str__(self):
        if self.expression.__str__() is not None:
            return self.expression.__str__()
