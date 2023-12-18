from io import TextIOWrapper
from typing import Set


class Extractor:
    def __init__(self) -> None:
        pass

    def export(self, string: str, file: TextIOWrapper):
        file.write(string)

    def extract(
        self,
        lookup_set: Set[str],
        key: str,
        filename: str,
        output_file: str
    ):
        export_file = open(output_file, 'w+')
    
        with open(filename, 'r') as file:
            columns_raw = file.readline()
            columns = columns_raw.replace('"', '') \
                                .strip() \
                                .split(',')
            try:
                index_of_key = columns.index(key)
            except ValueError as e:
                print(e)
                print(f" ERROR: key {key} not found in {filename} columns ")
                exit(1)

            self.export(columns_raw, export_file)
            
            for line in file:
                line = line.replace('"', '') \
                        .strip() \
                        .split(',')
                if line[index_of_key] in lookup_set:
                    line = [f'"{string}"' for string in line]
                    line = ",".join(line)
                    self.export(line + "\n", export_file)

