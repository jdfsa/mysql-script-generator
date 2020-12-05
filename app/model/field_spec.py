from typing import TypedDict, Any

class FieldSpec(TypedDict):
    """
    Tipo base para configuração dos campos
    """
    field_type: str
    length: int
    decimal: int
    serialize_pattern: str
    deserialize_pattern: str
    default_value: Any
    auto_generated: bool
    database_script: str