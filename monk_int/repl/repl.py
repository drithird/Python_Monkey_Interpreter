import monk_int.lexer.lexer as lexer
import monk_int.token.token as token


def repl():
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":
            break
        lex = lexer.New(str(user_input))
        while True:
            tok = lex.NextToken()
            print("Token Type: " + str(tok.Type) + " Literal: " + str(tok.Literal))
            if tok.Type == token.EOF:
                break
    return 0
