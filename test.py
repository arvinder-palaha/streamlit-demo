import pytest

from src.functions import parse_db_inspect_input

@pytest.mark.parametrize("input_string", [
    '',           # Empty input
    '  ',         # Whitespace
    ',,,',        # Just commas
    ', ,  ,   '   # Commas and whitespace
])
def test_parse_input_returns_empty_list(input_string):
    result = parse_db_inspect_input(input_string)
    assert isinstance(result, list)
    assert len(result) == 0

@pytest.mark.parametrize("input_string", [
    'db_name',
    ',db_name,',
    '  db_name  ',
    ' , db_name, '
])
def test_parse_input_returns_only_dbname(input_string):
    result = parse_db_inspect_input(input_string)
    assert len(result) == 1
    assert result[0] == 'db_name'
    
@pytest.mark.parametrize("input_string", [
    'db_name,col_name',
    'db_name, col_name  , ',
    ', ,db_name,col_name'
])
def test_parse_input_returns_2_keys(input_string):
    result = parse_db_inspect_input(input_string)
    assert result == ['db_name', 'col_name']