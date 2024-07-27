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

keywords: dict[str, TokenType] = {"fn": FUNCTION, "let": LET}


def LookupIdent(ident: str):
    if ident in keywords.keys():
        return keywords[ident]
    else:
        return IDENT
