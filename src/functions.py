from typing import List

def parse_db_inspect_input(input: str) -> List[str]:
    input_keys = [x for x in input.split(',') if len(x) > 0]
    return input_keys