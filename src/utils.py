def yes_no(value):
    return value.strip().upper() == "Y"

def contains(text, keyword):
    return keyword.lower() in text.lower() if text else False
