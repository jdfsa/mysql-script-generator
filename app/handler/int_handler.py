from typing import Any
from ..model.field_spec import FieldSpec

def int_handler(value: str, spec: FieldSpec) -> int:
    """
    Handler para campo do tipo Integer
    """
    if not(value):
        return 0

    if not(value.isnumeric()):
        raise ValueError(f'Esperado "int" no valor "{value}"')

    return int(value)

