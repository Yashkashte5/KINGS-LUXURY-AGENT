
# Kings Luxury Experience Agent

This project implements a **Level 2 AI Agent** for Kings Jewels, designed to generate a **Luxury Experience Pack** for each order. The agent behaves like a luxury experience strategist, synthesizing customer context, order details, and brand rules into actionable, brand-aligned outputs.

---

## Project Structure

```
Kings-Luxury-Experience-Agent/
│── README.md
│── main.py
│── requirements.txt
│
├── data/
│   ├── orders_level2.csv
│   └── kings_brand_rules.txt
│
├── outputs/
│   ├── luxury_experience.json
│   └── luxury_experience.txt
```

- `main.py` – Single entry point to run the agent and generate outputs.
- `data/` – Input CSV and brand rules text file.
- `outputs/` – Generated machine-readable and human-readable experience files.

---

## Features

- Reads orders and brand rules.
- Generates **persona summaries** per order.
- Determines **experience tier** based on order and customer context.
- Plans **packaging**, **unboxing**, and **post-delivery sequences**.
- Produces **WhatsApp & Email copy** tailored to the customer.
- Suggests **upsell recommendations** aligned with Kings brand.
- Flags **risks and assumptions** conservatively.
- Generates **JSON** and **human-readable text outputs**.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Yashkashte5/Kings-Luxury-Experience-Agent.git
cd Kings-Luxury-Experience-Agent

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

- This will read `data/orders_level2.csv` and `data/kings_brand_rules.txt`.
- Outputs will be written to `outputs/luxury_experience.json` and `outputs/luxury_experience.txt`.
- No external APIs are required; everything runs locally.

---

## Assumptions & Guardrails

- Missing customer notes: conservative defaults applied.
- Brand rules strictly enforced:
  - No hype, no aggressive selling, no exaggeration.
  - Discreet, refined, story-driven tone.
- Risk flags generated for unusual or urgent requests.
- Agent adapts to new datasets without code changes.

---

## Outputs

- `luxury_experience.json` – Structured, machine-readable experience plan per order.
- `luxury_experience.txt` – Human-readable operations sheet for the Kings team.

---

## Author

**Yash Kashte**  

## Note
Level 2 Submission
