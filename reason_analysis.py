# part_c_reason_analysis.py
# Step C: Return strength + specific reasons for weakness

common_4_digit_mpin = [
    "0000", "1111", "1234", "4321", "1122", "1212", "2222",
    "3333", "4444", "5555", "6666", "7777", "8888", "9999",
    "1010", "2020", "2000", "1919", "6789", "0987"
]

def extract_patterns(date_str):
    try:
        parts = date_str.strip().split("-")
        if len(parts) != 3:
            return []
        dd, mm, yyyy = parts
        yy = yyyy[-2:]
        return [dd + mm, mm + dd, dd + yy, yy + dd, yyyy[-4:-2] + dd]
    except:
        return []

def evaluate_mpin(mpin, dob_self, dob_spouse, anniversary):
    reasons = []

    if mpin in common_4_digit_mpin:
        reasons.append("COMMONLY_USED")

    if mpin in extract_patterns(dob_self):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if mpin in extract_patterns(dob_spouse):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if mpin in extract_patterns(anniversary):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons

# Test
if __name__ == "__main__":
    mpin = input("Enter 4-digit MPIN: ")
    dob_self = input("DOB: ")
    dob_spouse = input("Spouse DOB: ")
    anniversary = input("Anniversary: ")

    strength, reasons = evaluate_mpin(mpin, dob_self, dob_spouse, anniversary)
    print("Strength:", strength)
    print("Reasons:", reasons)
