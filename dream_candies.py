'''
INPUT: The input of the tool is the customers sample input file (see Chapter 1.2)
EXP OUTPUT: three smaller files containing the extracted customer data from the full extraction
'''

from typing import Type
from extraction_strategy import ExtractionStrategy, CustomerInvoicesExtractionStrategy



class DreamCandy:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy: Type[ExtractionStrategy]):
        self.__strategy = strategy

    def extract_files(self):
        self.__strategy.implement()


if __name__ == '__main__':
    app = DreamCandy()
    customer_strategy = CustomerInvoicesExtractionStrategy()
    app.set_strategy(customer_strategy)
    app.extract_files()
