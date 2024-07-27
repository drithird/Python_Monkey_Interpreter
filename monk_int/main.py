import monk_int.repl.repl as repl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--interactive",
    action=argparse.BooleanOptionalAction,
    help="Start an active terminal with the Python Monkey Lang Interpreter",
)
command = parser.parse_args()
if command.interactive:
    repl.repl()
