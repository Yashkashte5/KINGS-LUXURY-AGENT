import csv

def load_orders(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_brand_rules(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
