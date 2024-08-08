from typing import List

def parse_db_inspect_input(input: str) -> List[str]:
    input_keys = [x for x in input.split(',')]
    return input_keys