import re

visa_pattern = re.compile(r"^(?:4[0-9]{12}(?:[0-9]{3})?)$")
master_pattern = re.compile("^(?:5[1-5][0-9]{14})$")
amex_pattern = re.compile("^(?:3[47][0-9]{13})$")

while True:
    try:
        n = int(input("Number:"))
    except ValueError:
        continue

    if re.match(visa_pattern, str(n)):
        print("VISA")
    elif re.match(master_pattern, str(n)):
        print("MASTERCARD")
    elif re.match(amex_pattern, str(n)):
        print("AMEX")
    else:
        print("INVALID")

    break
