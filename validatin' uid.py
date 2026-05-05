import re
def is_valid_uid(uid):
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    if not re.match(r'^[a-zA-Z0-9]{10}$', uid):
        return False
    if len(set(uid)) != 10:
        return False    
    return True
n = int(input())
for _ in range(n):
    if is_valid_uid(input()):
        print("Valid")
    else:
        print("Invalid")
