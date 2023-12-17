from typing import Set
from utils.import read_lines_from

class Extractor:
    def __init__(self, type, data_file) -> None:
        pass
    
    def extract(filename: str, output_path: str):
        pass

class CustomerExtractor(Extractor):
    """Extract customer data using customer_sample"""
    def extract(samples: Set[str], filename: str, output_file):
        for line in read_lines_from(filename):
            customer_reccord = to_dict(line)
            if customer_reccord['CUSTOMER_CODE'] in samples:
                Exporter.export(customer_reccord, output_file)

class InvoiceExtractor(Extractor):
    """Extract invoices data using customer_sample"""
    def extract(samples: Set[str], filename: str, output_path):
        for line in read_lines_from(filename):
            invoice_reccord = to_dict(line)
            if invoice_reccord['CUSTOMER_CODE'] in samples:
                Exporter.export(invoice_reccord, output_file)
    

class InvoiceItemExtractor(Extractor):
    """Extract invoices items using invoices sapmle"""
    def extract(sample: Set[str], filename: str, output_path):
        for line in read_lines_from(filename):
            invoice_item_reccord = to_dict(line)
            if invoice_item_reccord['CUSTOMER_CODE'] in samples:
                Exporter.export(invoice_item_reccord, output_file)
