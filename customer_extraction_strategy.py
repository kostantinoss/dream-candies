
from typing import Type
from dream_candies import ExtractionStrategy
from extractor import CustomerExtractor, InvoiceExtractor, InvoiceItemExtractor

class CustomerInvoicesExtractionStrategy(ExtractionStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.__extractor = None

    def implement(self):
        # 1. sample customers
        customer_sample = create_set(
            filename='data/input/customer_sample.csv',
            key='CUSTOMER_CODE'
        )

        customer_extractor = CustomerExtractor()
        customer_extractor.extract(
            samples=customer_sample,
            filename='data/input/customers.csv',
            output_file='data/output/customers.csv'
        )

        invoices_extractor = InvoiceExtractor()
        invoices_extractor.extract(
            samples=customer_sample,
            filename='data/input/invoice.csv',
            output_file='data/input/invoice.csv'
        )

        invoices = create_set(
            filename='data/input/customer_sample.csv',
            key='INVOICE_CODE'
        )

        invoice_items_extractor = InvoiceItemExtractor()
        invoice_items_extractor.extract(
            samples=invoices,
            filename='data/input/invoice_items.csv',
            output_file='data/output/invoice_items.csv'
        )

        print("CustomerInvoicesExtractionStrategy")
        pass
    
    def sample_customers(self):
        pass