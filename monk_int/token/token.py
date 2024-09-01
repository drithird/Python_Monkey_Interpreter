class TokenType:
    def __init__(self, token_type: str):
        self.token_type = token_type


class Token:
    def __init__(self, type: TokenType, literal: str):
        self.Type: TokenType = type
        self.Literal: str = literal


ILLEGAL = "ILLEGAL"
EOF = "EOF"
# Identifiers + Literals,
IDENT = "IDENT"
INT = "INT"
# Operators
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"
EQ = "=="
NOT_EQ = "!="
LT = "<"
GT = ">"
# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
# Keywords
FUNCTION = "FUNCTION"
LET = "LET"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"

keywords: dict[str, TokenType] = {
    "fn": FUNCTION,
    "let": LET,
    "true": TRUE,
    "false": FALSE,
    "if": IF,
    "else": ELSE,
    "return": RETURN,
}


def LookupIdent(ident: str):
    if ident in keywords.keys():
        return keywords[ident]
    else:
        return IDENT
