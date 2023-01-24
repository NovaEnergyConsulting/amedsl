from textx import scoping
import amedsl


def print_props(obj):
    if (hasattr(obj, "__dict__")):
        for prop, value in vars(obj).items():
            print(f"<{prop}:{value}>\n")


def print_attr_props(obj, attr):
    if (hasattr(obj, attr)):
        print_props(getattr(obj, attr))
    else:
        print(f"{attr} attribute not found in {obj}")


def print_statements(program):
    for stmt in program.statements:
        print(stmt)


def interpret():
    mm = amedsl.amedsl_language.metamodel()

    program = mm.model_from_file("examples/asset_class_definition.ame")

    print_statements(program)


interpret()
