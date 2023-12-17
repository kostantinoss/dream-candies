from typing import List


def read_lines_from(filename):
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            yield line

def get_csv_column_names(filename) -> List[str]:
    with open(filename, 'r') as file:
        return file.replace('"', '') \
                    .strip() \
                    .split(',')