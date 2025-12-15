from src.utils import yes_no, contains
from src.brand_engine import allowed_upsell, risk_assessment

VIP_THRESHOLD = 8000
SIGNATURE_THRESHOLD = 5000
ELEVATED_THRESHOLD = 3000

def infer_experience_tier(order):
    value = float(order["OrderValueUSD"])

    if value >= VIP_THRESHOLD:
        return "VIP"
    if value >= SIGNATURE_THRESHOLD:
        return "Signature"
    if value >= ELEVATED_THRESHOLD or order["DeliverySpeed"].lower() == "urgent":
        return "Elevated"
    return "Standard"

def persona_summary(order):
    return (
        ("First-time Kings customer. " if yes_no(order["FirstTimeCustomer"]) else "Returning Kings client. ")
        + f"Located in {order['City']}, {order['Country']}. "
        + f"Engaged via {order['Channel']}."
    )

def packaging_plan(order, tier):
    if contains(order["CustomerNotes"], "minimal"):
        return "Minimal, understated Kings packaging with precision finish"

    if tier in ["VIP", "Signature"]:
        return "Understated luxury packaging with enhanced detailing"

    if tier == "Elevated":
        return "Premium Kings packaging, restrained and precise"

    return "Standard Kings packaging with clean presentation"

def unboxing_details(tier):
    if tier in ["VIP", "Signature"]:
        return "Calm unboxing with subtle reveal and tactile emphasis"
    if tier == "Elevated":
        return "Smooth unboxing highlighting craftsmanship"
    return "Simple, elegant unboxing without excess"

def communication_copy(tier):
    base = "Thank you for choosing Kings. Your piece has been prepared with care and discretion."

    if tier in ["VIP", "Signature"]:
        base += " We trust it will become part of your personal story."

    whatsapp = base
    email = base + " Should you require any assistance, our team remains at your service."

    return whatsapp, email

def post_delivery_sequence():
    return {
        "Day 1": "Delivery confirmation and care availability check",
        "Day 7": "Ownership guidance and craftsmanship care note",
        "Day 21": "Quiet follow-up ensuring long-term satisfaction"
    }

def generate_experience(order, brand_rules):
    tier = infer_experience_tier(order)
    persona = persona_summary(order)

    packaging = packaging_plan(order, tier)
    unboxing = unboxing_details(tier)
    whatsapp, email = communication_copy(tier)
    post_delivery = post_delivery_sequence()
    upsell = allowed_upsell(tier)
    risks = risk_assessment(order)

    decision_reasons = [
        f"Experience tier determined as {tier} based on order value and urgency",
        "Customer notes respected where explicitly stated",
        "Brand restraint prioritized over aggressive enhancement"
    ]

    if not order["CustomerNotes"]:
        decision_reasons.append("No customer notes provided; conservative defaults applied")

    json_block = {
        "persona_summary": persona,
        "experience_tier": tier,
        "packaging_plan": packaging,
        "unboxing_details": unboxing,
        "copy_whatsapp": whatsapp,
        "copy_email": email,
        "post_delivery_sequence": post_delivery,
        "upsell_recommendation": upsell,
        "risk_flags": risks,
        "decision_reasons": decision_reasons
    }

    text_block = f"""
ORDER {order['OrderID']}
Persona: {persona}
Experience Tier: {tier}

Packaging:
{packaging}

Unboxing:
{unboxing}

Customer Communication:
WhatsApp: {whatsapp}
Email: {email}

Post-Delivery:
Day 1: {post_delivery['Day 1']}
Day 7: {post_delivery['Day 7']}
Day 21: {post_delivery['Day 21']}

Upsell:
{upsell}

Risk Flags:
{', '.join(risks) if risks else 'None'}

Decision Rationale:
- """ + "\n- ".join(decision_reasons)

    return json_block, text_block.strip()
