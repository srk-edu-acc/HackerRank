import re

def validate_card(card):
    if not re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", card):
        return "Invalid"
    clean_card = card.replace("-", "")
    if re.search(r"(\d)\1{3,}", clean_card):
        return "Invalid"
    
    return "Valid"

n = int(input())
for _ in range(n):
    print(validate_card(input()))
