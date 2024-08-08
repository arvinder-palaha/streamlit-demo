import pytest

from src.functions import parse_db_inspect_input

def test_parse_input_returns_empty_list_when_given_empty_input():
    result = parse_db_inspect_input('')
    assert(isinstance(result, list))
    assert(0 == len(result))
    
def test_parse_input_returns_empty_list_when_given_whitespace():
    result = parse_db_inspect_input('  ')
    assert(0 == len(result))

def test_parse_input_returns_empty_list_when_given_just_commas():
    result = parse_db_inspect_input(',,,')
    assert(0 == len(result))

def test_parse_input_returns_empty_list_when_given_commans_and_whitespace():
    result = parse_db_inspect_input(', ,  ,   ')#
    assert(0 == len(result))