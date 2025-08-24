# part_a_common_checker.py
# Step A: Checks if the given 4-digit MPIN is commonly used

common_4_digit_mpin = [
    "0000", "1111", "1234", "4321", "1122", "1212", "2222",
    "3333", "4444", "5555", "6666", "7777", "8888", "9999",
    "1010", "2020", "2000", "1919", "6789", "0987"
]

def is_common_mpin(mpin):
    return mpin in common_4_digit_mpin

# Test
if __name__ == "__main__":
    mpin = input("Enter your 4-digit MPIN: ").strip()
    if is_common_mpin(mpin):
        print("⚠️ Common MPIN Detected!")
    else:
        print("✅ MPIN is not commonly used.")
