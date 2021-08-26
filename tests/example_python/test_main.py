'''
Example test script.
'''

from example_python.__main__ import get_execution_file

def test_get_execution_file():
    '''
    Simple test of one of the functions in the main code.
    '''
    result = get_execution_file()
    assert len(result) > 4
