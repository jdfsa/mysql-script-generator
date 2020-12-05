import os
from app import FlatTextProcessor
from app.helper import FileReader
from typing import Dict, Any

TABLE_NAME = 'TBL_EMPLOYEE'
SPEC_FILE_NAME = './files/employee_spec.json'
INPUT_FILE_NAME = './files/flat_file.txt'
OUTPUT_FILE_NAME = './files/output.sql'

flat_text_processor = FlatTextProcessor()

spec = FileReader().json_file(os.path.abspath(SPEC_FILE_NAME))

def init():
    
    with open(os.path.abspath(INPUT_FILE_NAME), 'r') as input_file, \
        open(os.path.abspath(OUTPUT_FILE_NAME), 'w') as output_file:

        for line in input_file:
            obj = flat_text_processor.parse(line, spec)
            
            fields = _script_fields(obj)
            script = _script(TABLE_NAME, fields)

            output_file.write(script)


def _script_fields(obj: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'ID': 'UUID()',
        'NAME': _quotes(obj['name']),
        'AGE': str(obj['age']),
        'BIRTH': _quotes(obj['birth']),
        'INCOME': str(obj['income']),
        'CREATION': _quotes(obj['creation'])
    }


def _quotes(value: Any) -> str:
    return "'" + value + "'"


def _script(table_name: str, fields: Dict[str, Any]) -> str:
    keys = ','.join(fields.keys())
    values = ','.join(fields.values())
    return f'insert into {table_name} ({keys}) values ({values});\n'


if __name__ == "__main__":
    init()