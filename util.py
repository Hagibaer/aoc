from typing import List, Union


def read_file_into_list(filepath: str, to_int: bool = False) -> List[Union[str, int]]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    if to_int:
        lines = [int(x) for x in lines]

    return lines
