import os
import json

class FileReader:
    """
    Leitor de arquivos
    """

    def json_file(self, filename, to_obj=True):
        """
        Lê um arquivo e retorna um JSON estruturado
        """
        abs_file_name = os.path.abspath(filename)
        with open(abs_file_name) as file:
            return json.load(file)
