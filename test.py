from unittest.mock import MagicMock
import pytest

from src.functions import parse_db_inspect_input, find_documents_from_collection

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
    
def test_parse_input_keeps_space_in_key():
    result = parse_db_inspect_input('db name, ')
    assert result == ['db name']


@pytest.mark.parametrize("search_dict, mock_documents, expected_result", [
    ({}, [], []),  # Empty collection with default search_dict
    ({}, [{'_id': 1, 'name': 'doc1'}, {'_id': 2, 'name': 'doc2'}], [{'_id': 1, 'name': 'doc1'}, {'_id': 2, 'name': 'doc2'}]),  # Non-empty collection with default search_dict
    ({'name': 'doc1'}, [{'_id': 1, 'name': 'doc1'}], [{'_id': 1, 'name': 'doc1'}]),  # Specific search_dict
    ({'name': 'nonexistent'}, [], []),  # No matching documents
    ({}, [{'_id': i, 'name': f'doc{i}'} for i in range(1000)], [{'_id': i, 'name': f'doc{i}'} for i in range(1000)])  # Large number of documents
])
def test_find_documents_from_collection(search_dict, mock_documents, expected_result):
    mock_collection = MagicMock()
    mock_collection.find.return_value = mock_documents
    
    result = find_documents_from_collection(mock_collection, search_dict)
    
    assert result == expected_result
    mock_collection.find.assert_called_once_with(search_dict)

def test_find_documents_from_collection_handles_exceptions():
    mock_collection = MagicMock()
    mock_collection.find.side_effect = Exception("Database error")
    
    with pytest.raises(Exception, match="Database error"):
        find_documents_from_collection(mock_collection)
    
    mock_collection.find.assert_called_once_with({})
