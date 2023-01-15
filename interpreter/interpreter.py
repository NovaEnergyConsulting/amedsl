from textx import scoping
import amedsl


def interpret():
    mm = amedsl.amedsl_language.metamodel()
    # for prop, value in vars(mm).items():
    #     print(f"<{prop}:{value}>")

    # mm.register_scope_providers({"*.*": scoping.providers.FQN()})
    program = mm.model_from_file("asset_class_definition.ame")

    print(program)

    for stmt in program.statements:
        print(f"Statement: {stmt}")

        # print("\tAttributes")
        # for attr in stmt.__dict__:
        #     print(f"\t{attr}: {stmt.__dict__[attr]}")

        #     if (hasattr(attr, "__dict__")):
        #         print(f"\t\t{attr.__dict__}")

        if (hasattr(stmt, "description")):
            print(f"\tName: {stmt.name}")
            print(f"\tDescription: {stmt.description}")

        if (hasattr(stmt, "asset_class")):
            print(f"\tAsset Class: {stmt.asset_class.name}")

        if (hasattr(stmt, "descriptors")):
            for descriptor in stmt.descriptors:
                if (hasattr(descriptor, 'name')):
                    print(f"\tDescriptor: {descriptor.name} {descriptor.type}")
                if (hasattr(descriptor, 'value')):
                    print(
                        f"\tDescriptor Instance: {descriptor.descriptor.name}: {descriptor.value}")

        if (hasattr(stmt, "components")):
            for component in stmt.components:
                print(f"\t\tComponent: {component.name}")

        if (hasattr(stmt, "unit_families")):
            for family in stmt.unit_families:
                print(f"\tFamily: {family.name} {family.description}")

        if (hasattr(stmt, "units")):
            print(
                f"\tName \t| Symbol \t| Family \t| Factor \t| Is Base?")
            for unit in stmt.units:
                # print(f"\t{unit}")
                print(
                    f"\t{unit.name} \t| {unit.symbol} \t| {unit.family.name} \t| {unit.factor} \t| {'is base' if unit.base else ''}")

    # print(f'Asset model: {model.name}')
    # if (hasattr(model, 'description')):
    #     print(model.description)

    # for ac in model.asset_classes:
    #     print()
    #     print(f'\tAsset Class: {ac.name}')
    #     print()
    #     print("\t***** Descriptors *****")
    #     for desc in ac.descriptors:
    #         print(f'\t{desc.name} type {desc.type}')
    #         if (desc.description != ""):
    #             print(f'\t\t{desc.description}')

    # for a in model.assets:
    #     print()
    #     print(f'\tAsset {a.name} of Asset Class {a.assetClass.name}')
    #     print()
    #     for desc in a.descriptors:
    #         print(f'\t{desc.descriptor.name} type {desc.descriptor.type}')
    #         if (desc.value != ""):
    #             print(f'\t\t{desc.value}')


interpret()
