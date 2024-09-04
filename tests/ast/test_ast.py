import monk_int.token.token as token
import monk_int.ast.ast as ast


def test_string():
    program = ast.Program()
    let_statement = ast.LetStatement(tok=token.Token(token.LET, "let"))
    let_statement.name = ast.Identifier(token.Token(token.IDENT, "myVar"), "myVar")
    let_statement.value = ast.Identifier(
        token.Token(token.IDENT, "anotherVar"), "anotherVar"
    )
    program.statements = [let_statement]
    print(program.__str__())
    assert program.__str__() == "let myVar = anotherVar;"
