from monk_int.token import token
from monk_int.lexer.lexer import New


def test_Lexer():
    input = "=+(){},;"

    tests = [
        [token.ASSIGN, "="],
        [token.PLUS, "+"],
        [token.LPAREN, "("],
        [token.RPAREN, ")"],
        [token.LBRACE, "{"],
        [token.RBRACE, "}"],
        [token.COMMA, ","],
        [token.SEMICOLON, ";"],
        [token.EOF, ""],
    ]

    l = New(input)
    for item in tests:
        tok = l.NextToken()
        assert tok.Type == item[0]
        assert tok.Literal == item[1]


def test_next_token():
    input = """
    let five = 5;
    let ten = 10;

    let add = fn(x,y) {
        x+y;
    };

    let result = add(five, ten);    """

    tests = [
        [token.LET, "let"],
        [token.IDENT, "five"],
        [token.ASSIGN, "="],
        [token.INT, "5"],
        [token.SEMICOLON, ";"],
        [token.LET, "let"],
        [token.IDENT, "ten"],
        [token.ASSIGN, "="],
        [token.INT, "10"],
        [token.SEMICOLON, ";"],
        [token.LET, "let"],
        [token.IDENT, "add"],
        [token.ASSIGN, "="],
        [token.FUNCTION, "fn"],
        [token.LPAREN, "("],
        [token.IDENT, "x"],
        [token.COMMA, ","],
        [token.IDENT, "y"],
        [token.RPAREN, ")"],
        [token.LBRACE, "{"],
        [token.IDENT, "x"],
        [token.PLUS, "+"],
        [token.IDENT, "y"],
        [token.SEMICOLON, ";"],
        [token.RBRACE, "}"],
        [token.SEMICOLON, ";"],
        [token.LET, "let"],
        [token.IDENT, "result"],
        [token.ASSIGN, "="],
        [token.IDENT, "add"],
        [token.LPAREN, "("],
        [token.IDENT, "five"],
        [token.COMMA, ","],
        [token.IDENT, "ten"],
        [token.RPAREN, ")"],
        [token.SEMICOLON, ";"],
        [token.EOF, ""],
    ]
    l = New(input)
    for item in tests:
        tok = l.NextToken()
        print(tok.Type, tok.Literal)
        assert tok.Type == item[0]
        assert tok.Literal == item[1]
