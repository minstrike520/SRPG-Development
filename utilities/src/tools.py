def is_intstr(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False

def spaces(amount):
    s = ""
    for i in range(amount):
        s += " "
    return s

def combine(li):
    s = ""
    for item in li:
        s += item+" "
    return s