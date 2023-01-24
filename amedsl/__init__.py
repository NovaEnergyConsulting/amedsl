import os
from textx import language, metamodel_from_file
from .object_processors import descriptor_instance_processor

__version__ = "0.0.1.dev"


@language('amedsl', '*.ame')
def amedsl_language():
    "amedsl language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'amedsl.tx'))

    # Register object processors
    obj_processors = {
        'DescriptorInstance': descriptor_instance_processor,
    }
    mm.register_obj_processors(obj_processors)

    return mm
