# part_b_demographic_check.py
# Step B: Check if MPIN is related to demographics (DOB etc.)

def extract_patterns(date_str):
    parts = date_str.strip().split("-")
    if len(parts) != 3:
        return []
    dd, mm, yyyy = parts
    yy = yyyy[-2:]
    return [dd + mm, mm + dd, dd + yy, yy + dd, yyyy[-4:-2] + dd]

def check_strength(mpin, dob_self, dob_spouse, anniversary):
    patterns = (
        extract_patterns(dob_self) +
        extract_patterns(dob_spouse) +
        extract_patterns(anniversary)
    )
    return "WEAK" if mpin in patterns else "STRONG"

# Test
if __name__ == "__main__":
    mpin = input("Enter your 4-digit MPIN: ").strip()
    dob_self = input("Enter DOB (dd-mm-yyyy): ")
    dob_spouse = input("Enter Spouse DOB (dd-mm-yyyy): ")
    anniversary = input("Enter Anniversary (dd-mm-yyyy): ")

    strength = check_strength(mpin, dob_self, dob_spouse, anniversary)
    print("🛡️ MPIN Strength:", strength)
