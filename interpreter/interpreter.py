from textx import scoping
import amedsl
from amedsl.object_processors import descriptor_instance_processor


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
    obj_processors = {
        'DescriptorInstance': descriptor_instance_processor,
    }
    mm.register_obj_processors(obj_processors)
    # mm.register_scope_providers({"*.*": scoping.providers.FQN()})
    program = mm.model_from_file("asset_class_definition.ame")

    print_statements(program)


interpret()
