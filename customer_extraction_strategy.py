
from typing import Set, Type
from dream_candies import ExtractionStrategy
from extractor import Extractor

class CustomerInvoicesExtractionStrategy(ExtractionStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._extractor = Extractor()

    def implement(self):
        customer_sample = self.create_set(
            filename='data/input/customer_sample.csv',
            key='CUSTOMER_CODE'
        )

        self._extractor.extract(
            lookup_set=customer_sample,
            key='CUSTOMER_CODE',
            filename='data/input/customers.csv',
            output_file='data/output/customers.csv'
        )

        self._extractor.extract(
            lookup_set=customer_sample,
            key='CUSTOMER_CODE',
            filename='data/input/invoice.csv',
            output_file='data/input/invoice.csv'
        )

        invoices = self.create_set(
            filename='data/input/customer_sample.csv',
            key='INVOICE_CODE'
        )

        self._extractor.extract(
            lookup_set=invoices,
            key='INVOICE_CODE',
            filename='data/input/invoice_items.csv',
            output_file='data/output/invoice_items.csv'
        )

        print("CustomerInvoicesExtractionStrategy")
    
    def create_set(filename: str, key: str) -> Set[str]:
        """
        Creates a set from a `.csv` file containing the values under `key` column
        """
        output = set()
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
                line = line.replace('"', '') \
                            .strip() \
                            .split(',')
                output.add(line[index_of_key])
        
        return output