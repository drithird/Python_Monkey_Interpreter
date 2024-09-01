import monk_int.lexer.lexer as lexer
import monk_int.parser.parser as parser
import monk_int.ast.ast as ast
from monk_int.ast.ast import LetStatement
import pytest


@pytest.mark.timeout(3)
def test_let_statements():
    input = """
        let x = 5;
        let y = 10;
        let foobar = 838383;
    """
    tests = [
        {"expected_identifier": "x"},
        {"expected_identifier": "y"},
        {"expected_identifier": "foobar"},
    ]

    lex = lexer.New(input)
    parse: parser.Parser = parser.Parser(lex)

    program = parse.parse_program()
    assert program is not None, "ParseProgram() returned none"
    assert (
        len(program.statements) == 3
    ), f"program.statements does not contain 3 statements. got {len(program.statements)}"

    for i, item in enumerate(tests):
        statement = program.statements[i]
        assert help_test_let_statement(
            statement, item["expected_identifier"]
        ), f"test_let_statement failed for expected identifier {item["expected_identifier"]}"


def help_test_let_statement(statement: LetStatement, expected_identifier: str):
    assert isinstance(
        statement, ast.LetStatement
    ), f"s not LetStatement. got={type(statement)}"
    assert (
        statement.token_literal() == "let"
    ), f"s.token_literal not 'let'. got={statement.token_literal()}"

    let_stmt = statement
    assert (
        let_stmt.name.value == expected_identifier
    ), f"letStmt.name.value not '{expected_identifier}'. got={let_stmt.name.value}"
    assert (
        let_stmt.name.token_literal() == expected_identifier
    ), f"letStmt.name.token_literal() not '{expected_identifier}'. got={let_stmt.name.token_literal()}"

    return True
