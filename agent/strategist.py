import json
from agent.prompts import SYSTEM_PROMPT, USER_PROMPT
from agent.llm_client import call_llm

def generate_experience(order: dict, brand_rules: str, max_retries=3) -> dict:
    """
    Generates a luxury experience for a single order using a multi-step AI Agent approach.
    Python only handles I/O, retries, and JSON validation.
    """

    user_prompt = USER_PROMPT.format(
        brand_rules=brand_rules,
        order_json=json.dumps(order, indent=2)
    )

    for attempt in range(max_retries):
        raw_response = call_llm(SYSTEM_PROMPT, user_prompt)
        try:
            experience = json.loads(raw_response)
            # Validate required fields
            required_fields = [
                "persona_summary", "experience_tier", "packaging_plan",
                "unboxing_details", "copy_whatsapp", "copy_email",
                "post_delivery_sequence", "upsell_recommendation",
                "risk_flags", "decision_reasons"
            ]
            for field in required_fields:
                if field not in experience:
                    # Fill intelligently if missing
                    experience[field] = [] if field in ["risk_flags", "decision_reasons"] else "N/A"
            return experience
        except json.JSONDecodeError:
            if attempt == max_retries - 1:
                raise ValueError(f"LLM returned invalid JSON after {max_retries} attempts:\n{raw_response}")
            # Retry if invalid JSON
            continue

def generate_experiences_for_orders(orders: list, brand_rules: str) -> list:
    """
    Generates AI Agent experiences for multiple orders.
    """
    results = []
    for order in orders:
        experience = generate_experience(order, brand_rules)
        order_id = order.get("order_id", "UNKNOWN")
        results.append({"order_id": order_id, "experience": experience})
    return results
