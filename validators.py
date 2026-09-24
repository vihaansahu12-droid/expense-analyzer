# validators.py
# Checks user input before it is used. Uses only if statements and string methods 


def is_valid_amount(value):
    # value is a string coming from input()
    # remove one decimal point and one minus sign, then check if the
    # remaining characters are all digits
    cleaned = value.replace(".", "", 1)
    cleaned = cleaned.replace("-", "", 1)
    if cleaned.isdigit() == False:
        return False
    if float(value) <= 0:
        return False
    return True


def is_non_empty(text):
    if text.strip() == "":
        return False
    return True
