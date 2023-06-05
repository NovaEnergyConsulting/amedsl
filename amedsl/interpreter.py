import amedsl
from textx import textx_isinstance


def print_props(obj):
    if (hasattr(obj, "__dict__")):
        for prop, value in vars(obj).items():
            print(f"<{prop}:{value}>\n")


def print_attr_props(obj, attr):
    if (hasattr(obj, attr)):
        print_props(getattr(obj, attr))
    else:
        print(f"{attr} attribute not found in {obj}")


def recursively_print_assets(root_asset, level=0):
    print(f"{'|-- '*level}{root_asset}")
    for asset in root_asset.assets:
        recursively_print_assets(asset, level+1)


def print_statements(program, printprops=False):
    for stmt in program.statements:

        mm = amedsl.amedsl_language.metamodel()
        if (textx_isinstance(stmt, mm['Asset'])):
            print()
            recursively_print_assets(stmt)

        if (printprops):
            print_props(stmt)
