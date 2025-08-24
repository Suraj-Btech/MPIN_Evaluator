# part_d_6digit_support.py
# Step D: Add support for 6-digit MPINs

common_mpin_list = [
    # 4-digit
    "0000", "1111", "1234", "4321", "1122", "1212",
    "2222", "3333", "4444", "5555", "6666", "7777",
    "8888", "9999", "1010", "2020", "2000", "1919", "6789", "0987",
    # 6-digit
    "123456", "111111", "000000", "999999", "121212",
    "112233", "654321", "102030", "202020", "111222"
]

def extract_patterns(date_str, pin_length):
    try:
        parts = date_str.strip().split("-")
        if len(parts) != 3:
            return []
        dd, mm, yyyy = parts
        yy = yyyy[-2:]
        if pin_length == 4:
            return [dd + mm, mm + dd, dd + yy, yy + dd, yyyy[-4:-2] + dd]
        elif pin_length == 6:
            return [dd + mm + yy, yy + mm + dd, mm + dd + yy, dd + yy + mm, yy + dd + mm]
        else:
            return []
    except:
        return []

def evaluate_mpin(mpin, dob_self, dob_spouse, anniversary):
    pin_length = len(mpin)
    reasons = []

    if mpin in common_mpin_list:
        reasons.append("COMMONLY_USED")

    if dob_self and mpin in extract_patterns(dob_self, pin_length):
        reasons.append("DEMOGRAPHIC_DOB_SELF")

    if dob_spouse and mpin in extract_patterns(dob_spouse, pin_length):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")

    if anniversary and mpin in extract_patterns(anniversary, pin_length):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons


# Test
if __name__ == "__main__":
    mpin = input("Enter your MPIN (4 or 6 digits): ")
    dob_self = input("Your DOB: ")
    dob_spouse = input("Spouse DOB: ")
    anniversary = input("Anniversary: ")

    strength, reasons = evaluate_mpin(mpin, dob_self, dob_spouse, anniversary)
    print("Strength:", strength)
    print("Reasons:", reasons)
