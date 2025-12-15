import json
from src.loader import load_orders, load_brand_rules
from src.experience_engine import generate_experience

DATA_DIR = "data"
OUTPUT_DIR = "outputs"

def main():
    orders = load_orders(f"{DATA_DIR}/orders_level2.csv")
    brand_rules = load_brand_rules(f"{DATA_DIR}/kings_brand_rules.txt")

    luxury_json = {}
    luxury_text_blocks = []

    for order in orders:
        json_block, text_block = generate_experience(order, brand_rules)
        luxury_json[order["OrderID"]] = json_block
        luxury_text_blocks.append(text_block)

    with open(f"{OUTPUT_DIR}/luxury_experience.json", "w", encoding="utf-8") as f:
        json.dump(luxury_json, f, indent=2)

    with open(f"{OUTPUT_DIR}/luxury_experience.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(luxury_text_blocks))

    print("Luxury experience outputs generated successfully.")

if __name__ == "__main__":
    main()
