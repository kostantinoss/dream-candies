from typing import Set
from exporter import Exporter


class Extractor:
    def __init__(self) -> None:
        pass
    
    def extract(
        lookup_set: Set[str],
        key: str,
        filename: str,
        output_file: str
    ):
        with open(filename, 'r') as file:
            columns = file.readline()
            columns = columns.replace('"', '') \
                        .strip() \
                        .split(',')
            try:
                index_of_key = columns.index(key)
            except ValueError as e:
                print(e)
                print(f" ERROR: key {key} not found in {filename} columns ")
                return 1
            
            for line in file:
                if line[index_of_key] in lookup_set:
                    Exporter.export(line, output_file)

