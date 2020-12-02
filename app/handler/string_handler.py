from typing import Any
from ..model.field_spec import FieldSpec

def string_handler(value: str, spec: FieldSpec) -> str:
    """
    Handler para campo do tipo String
    """
    if not(value): value = ''

    return value.strip()
