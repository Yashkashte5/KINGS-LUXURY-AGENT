import pandas as pd
import json
from agent.strategist import generate_experiences_for_orders

def extract_order_id(order: dict) -> str:
    order_id = order.get("OrderID") or order.get("order_id")
    if not order_id:
        raise ValueError("Order ID missing from input data")
    return str(order_id)

def main():
    # Load orders from CSV
    orders = pd.read_csv("data/orders_level2.csv").to_dict(orient="records")

    # Load Kings brand rules for AI context
    with open("data/kings_brand_rules.txt", "r", encoding="utf-8") as f:
        brand_rules = f.read()

    # Generate AI Agent experiences
    all_outputs = generate_experiences_for_orders(orders, brand_rules)

    # Ensure every order has correct ID
    for i, order in enumerate(orders):
        if all_outputs[i]["order_id"] == "UNKNOWN":
            all_outputs[i]["order_id"] = extract_order_id(order)

    # Save as JSON
    with open("outputs/luxury_experience.json", "w", encoding="utf-8") as f:
        json.dump(all_outputs, f, indent=2, ensure_ascii=False)

    # Save human-readable TXT for review
    with open("outputs/luxury_experience.txt", "w", encoding="utf-8") as f:
        for item in all_outputs:
            f.write(f"Order ID: {item['order_id']}\n")
            f.write(json.dumps(item["experience"], indent=2, ensure_ascii=False))
            f.write("\n\n")

    print("Luxury experiences generated successfully!")

if __name__ == "__main__":
    main()
