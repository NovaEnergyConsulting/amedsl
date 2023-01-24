from textx import TextXSemanticError


def descriptor_instance_processor(descriptor_instance):
    name = descriptor_instance.descriptor.name
    type = descriptor_instance.descriptor.type
    val = descriptor_instance.value

    if (descriptor_instance.descriptor.type == 'number'):
        if (not (isInt(val) or isFloat(val))):
            raiseTypeError(name, val, type)

    elif (descriptor_instance.descriptor.type == 'text'):
        if (not isStr(val)):
            raiseTypeError(name, val, type)

    elif (descriptor_instance.descriptor.type == 'quantity'):
        if (not isQuantity(val)):
            raiseTypeError(name, val, type)


def raiseTypeError(name, val, type):
    raise TextXSemanticError(
        f"Incorrect property type: The property {name} with value {val} is expected to be of type '{type}'.")


def isStr(val):
    return type(val) is str


def isInt(val):
    return type(val) is int


def isFloat(val):
    return type(val) is float


def isQuantity(val):
    if (hasattr(val, "__class__")):
        return (val.__class__.__name__ == 'Quantity')
