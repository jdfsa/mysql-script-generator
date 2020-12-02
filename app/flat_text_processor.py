from typing import Any, Mapping, Callable
from .model import FieldSpec
from .handler import datetime_handler, float_handler, int_handler, string_handler

class FlatTextProcessor:
    """
    Conversor de objeto em posicional
    """

    def __init__(self):
        self.__init_handlers()


    def parse(self, flat_text: str, spec: Mapping[str, FieldSpec]) -> Mapping[str, Any]:
        self.__validate_args(flat_text, spec)

        ret = {}
        last_position = 0

        for field in spec:
            field_spec = spec[field]
            handler = self.__get_handler(field_spec['field_type'])

            position_start = last_position
            position_end = last_position + field_spec['length']

            value = flat_text[position_start:position_end]

            ret[field] = handler(value, field_spec)

            last_position += field_spec['length']

        return ret


    def __validate_args(self, flat_text: str, spec: Mapping[str, FieldSpec]) -> None:
        """
        Valida os parâmetros de entrada
        """
        if not(flat_text):
            raise ValueError('Invalid flat text')
        if not(spec):
            raise ValueError('JSON specifications not informed')


    def __init_handlers(self) -> None:
        """
        Define em 'self' a lista de handlers que serão utilizados
        """
        self._handlers = {
            'string': string_handler,
            'int': int_handler,
            'float': float_handler,
            'date': datetime_handler,
            'datetime': datetime_handler
        }


    def __get_handler(self, name: str) -> Callable:
        """
        Obtém um type handler com base no nome do tipo
        """
        handler = self._handlers.get(name)
        if not(handler):
            raise Exception('Handler não definido para o tipo: {name}')
        return handler