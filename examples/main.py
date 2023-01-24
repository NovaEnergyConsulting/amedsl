import amedsl
from src.interpreter import interpret


def repl():
    print("\nAME.DSL REPL v0.1")

    try:
        while True:
            try:
                _in = input("enter file to run>")
                try:
                    interpret()
                    # print(eval(_in))
                except:
                    out = exec(_in)
                    if out != None:
                        print(out)
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt as e:
        print("\nExiting ...")


repl()
