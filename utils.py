from typing import Dict, List, Set


def lookup_set() -> Set[str]:
    return

def to_dict() -> Dict[str, str]:
    return

def read_lines_from(filename) -> None:
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            yield line

def get_csv_column_names(filename) -> List[str]:
    with open(filename, 'r') as file:
        return file.replace('"', '') \
                    .strip() \
                    .split(',')