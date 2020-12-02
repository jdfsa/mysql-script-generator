from context import FileReader, FlatTextProcessor

import unittest
import json

class FlatTextProcessorTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        f_reader = FileReader()
        
        self.__data = {
            'test_case': f_reader.json_file('test_cases/test_case.json'),
            'spec': f_reader.json_file('spec/employee_spec.json')
        }
        
        self.__processor = FlatTextProcessor()

    def test_parse(self):
        test_case = self.__data['test_case']
        spec = self.__data['spec']

        result = self.__processor.parse(
            flat_text=test_case['flat'], 
            spec=spec
        )

        self.assertEqual(result, test_case['obj'])

if __name__ == '__main__':
    unittest.main()
