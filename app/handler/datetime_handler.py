import arrow
from typing import Any
from ..model.field_spec import FieldSpec

def datetime_handler(value: str, spec: FieldSpec) -> str:
    """
    Handler para campo do tipo Date/DateTime    
    """
    if not(value):
        return value
    
    date_value = arrow.get(value, spec['flat_pattern'])    
    
    return date_value.format(spec['object_pattern'])


def __init_defaults(spec: FieldSpec) -> tuple:
    """
    Inicializa os pattern default e retorna uma tupla na ordem
    1. flat_pattern
    2. object_pattern
    
    Caso não informado, para cada item deve retornar como default o pattern 'YYYY-MM-DD'
    """
    date_default_pattern = "YYYY-MM-DD"
    flat_pattern = spec['flat_pattern'] if spec and spec['flat_pattern'] else date_default_pattern
    object_pattern = spec['object_pattern'] if spec and spec['object_pattern'] else date_default_pattern

    return flat_pattern, object_pattern
