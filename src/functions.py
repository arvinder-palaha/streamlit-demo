from typing import List

def parse_db_inspect_input(input: str) -> List[str]:
    split_input = input.split(',')
    stripped_split_input = [x.lstrip().rstrip() for x in split_input]
    filtered_stripped_split_input = [x for x in stripped_split_input if len(x)>0]
    return filtered_stripped_split_input