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