import monk_int.lexer.lexer as lexer
import monk_int.parser.parser as parser
import monk_int.ast.ast as ast
from monk_int.ast.ast import LetStatement
import pytest


def test_parser_errors():
    input = """
        let  = 5;
        let  = ;
        let foobar 838383;
    """
    tests = [
        "expected next token to be IDENT, got = instead",
        "expected next token to be IDENT, got = instead",
        "expected next token to be =, got INT instead",
    ]
    lex = lexer.New(input)
    parse: parser.Parser = parser.Parser(lex)
    parse.parse_program()
    errors = parse.Errors()
    for index, error in enumerate(errors):
        assert error == tests[index]


def check_parser_errors(parse: parser.Parser):
    errors = parse.Errors()
    if len(errors) == 0:
        return
    print(f"parser has {len(errors)} errors")
    for error in errors:
        print(error)
    assert False


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
    check_parser_errors(parse)
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


def test_return_statements():
    input = """
    return 5;
    return 10;
    return 993322;
    """

    lex = lexer.New(input)
    parse: parser.Parser = parser.Parser(lex)
    program = parse.parse_program()
    check_parser_errors(parse)

    assert len(program.statements) == 3
    for stmt in program.statements:
        assert isinstance(
            stmt, ast.ReturnStatement
        ), f"improper statement type returned type '{type(stmt)}'"
        assert (
            stmt.token_literal() == "return"
        ), f"return statement did not return the token literal 'return' it returned '{stmt.token_literal()}' instead"


def test_identifier_expression():
    input = "foobar;"
    lex = lexer.New(input)
    parse = parser.Parser(lex)
    program = parse.parse_program()
    check_parser_errors(parse)
    assert (
        len(program.statements) == 1
    ), f"Program has an imprproper amount of spaces it should be 1 returned {len(program.statements)} "
    statement = program.statements[0]
    assert isinstance(
        statement, ast.ExpressionStatement
    ), f"Statment did not return proper ExpressionStatement returned {type(statement)} instead"
    ident = statement.expression
    assert isinstance(
        ident, ast.Identifier
    ), f"Statment did not return proper Identifier returned {type(statement)} instead"
    assert (
        ident.value == "foobar"
    ), f"Identifier.value is not correct should have returned foobar returned {ident.value}"
    assert (
        ident.token_literal() == "foobar"
    ), f"Identifier.token_literal is not correct should have returned foobar returned {ident.token_literal()}"
