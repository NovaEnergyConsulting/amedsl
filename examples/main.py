import amedsl
from amedsl.interpreter import print_statements, print_props


def repl():
    print("\namedsl REPL v0.1")

    try:
        while True:
            try:
                _in = input("enter file to run>")
                mm = amedsl.amedsl_language.metamodel()
                program = mm.model_from_file(_in)
                print_statements(program)
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt as e:
        print("\nExiting ...")


repl()
