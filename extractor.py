from typing import Set


class Extractor:
    def __init__(self, type, data_file) -> None:
        pass
    
    def extract(filename: str, output_path: str):
        pass

class CustomerExtractor(Extractor):
    """Extract customer data using customer_sample"""
    def extract(samples: Set[str], filename: str, output_path: str):
        return super().extract(output_path)

class InvoiceExtractor(Extractor):
    """Extract invoices data using customer_sample"""
    def extract(samples: Set[str], filename: str, output_path: str):
        return super().extract(output_path)
    

class InvoiceItemExtractor(Extractor):
    """Extract invoices items using invoices sapmle"""
    def extract(sample: Set[str], filename: str, output_path: str):
        return super().extract(output_path)

