import re
from typing import Any
from ..model.field_spec import FieldSpec

def float_handler(value: str, spec: FieldSpec) -> float:
    """
    Handler para campo do tipo Float
    """
    if not(value):
        return 0.0

    if not re.findall('^[0-9.]+$', value):
        raise ValueError(f'Esperado "float" no valor "{value}"')
    
    decimals = spec['decimals']
    string_value = f'{value[0:-decimals]}.{value[-decimals:len(value)]}'

    return float(string_value)
