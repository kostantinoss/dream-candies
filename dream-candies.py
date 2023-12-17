'''
INPUT: The input of the tool is the customers sample input file (see Chapter 1.2)
EXP OUTPUT: three smaller files containing the extracted customer data from the full extraction
'''

from typing import List, Set

def dream_candy(customer_sample_filename, customers_filename, invoice_filename, invoice_items_filename):
    customers_sample = init_customers_samples(customer_sample)
    extract_customers(customer_sample, customers, invoice_filename, invoice_items_filename)
    extract_invoices(customers_sample, invoice_filename)
    extract_invoice_items(invoices_sample, invoice_items_filename)

def extract_invoices(customers_sample, invoice_filename):
    # extract invoices using customer_sample
    for line in read_lines_from(invoice_filename):
        line = line.replace('"', '') \
                    .strip() \
                    .split(',')
        if line[0] in customers_sample:
            print(line)

def extract_customers(customers_sample, customers_filename):
    # extract customers using customer_sample
    for line in read_lines_from(customers_filename):
        line = line.replace('"', '') \
                    .strip() \
                    .split(',')
        if line[0] in customers_sample:
            print(line)

def extract_invoice_items(invoices_sample, invoice_items_filename):
    # extract invoice_items using invoices
    for line in read_lines_from(invoice_items_filename):
        line = line.replace('"', '') \
                    .strip() \
                    .split(',')
        if line[0] in invoices_sample:
            print(line)

def init_customers_samples(
        customer_sample_filename,
        customers_filename,
        invoice_filename,
        invoice_items_filename) -> Set[str]:
    customers_sample = set()
    for customer in read_lines_from(customer_sample_filename):
        customer = customer.replace('"', '') \
                            .strip()
        customers_sample.add(customer)
    return customer_sample

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
    

if __name__ == '__main__':
    customer_sample = 'data/customer_sample.csv'
    customers = 'data/customers.csv'
    invoice = 'data/invoice.csv'
    invoice_items = 'data/invoice_items.csv'
    dream_candy(customer_sample, customers, invoice, invoice_items)
