import amedsl
import type_checking

mm = amedsl.amedsl_language.metamodel()
model = mm.model_from_file("interpreter/test.ame")

print(f'Asset model: {model.name}')
if(hasattr(model,'description')): print(model.description)

for ac in model.asset_classes:
    print()
    print(f'\tAsset Class: {ac.name}')
    print()
    print("\t***** Descriptors *****")
    for desc in ac.descriptors:
        print(f'\t{desc.name} type {desc.type}')
        if(desc.description != ""):  print(f'\t\t{desc.description}')

for a in model.assets:
    print()
    print(f'\tAsset {a.name} of Asset Class {a.assetClass.name}')
    print()
    for desc in a.descriptors:
        print(f'\t{desc.descriptor.name} type {desc.descriptor.type}')
        if(desc.value != ""):  print(f'\t\t{desc.value}')