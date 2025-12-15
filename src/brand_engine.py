def allowed_upsell(tier):
    if tier in ["VIP", "Signature"]:
        return "Future bespoke customization consultation"
    if tier == "Elevated":
        return "Care and maintenance guidance for long-term ownership"
    return "No upsell recommended"

def risk_assessment(order):
    risks = []

    if order["DeliverySpeed"].lower() == "urgent":
        risks.append("Delivery expectations require careful management")

    if "discreet" in order["CustomerNotes"].lower():
        risks.append("Heightened discretion required")

    return risks
