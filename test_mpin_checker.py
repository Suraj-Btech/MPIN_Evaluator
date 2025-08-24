# test_mpin_checker.py
# Step 5: Run 20+ test cases

from part_d_6digit_support import evaluate_mpin

def run_test(i, mpin, dob1, dob2, anniv, expected_strength, expected_reasons):
    strength, reasons = evaluate_mpin(mpin, dob1, dob2, anniv)
    passed = strength == expected_strength and sorted(reasons) == sorted(expected_reasons)
    print(f"Test {i}: {'✅' if passed else '❌'}")
    if not passed:
        print(f"  → MPIN: {mpin}")
        print(f"  → Expected: {expected_strength}, {expected_reasons}")
        print(f"  → Got:      {strength}, {reasons}")

tests = [
    ("1234", "01-02-1998", "03-04-1996", "05-06-2015", "WEAK", ["COMMONLY_USED"]),
    ("0201", "02-01-1998", "03-03-2000", "01-01-2020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("0304", "01-02-1998", "03-04-2000", "01-01-2020", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("0506", "01-02-1998", "03-04-2000", "05-06-2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("9999", "01-01-2000", "01-01-2000", "01-01-2000", "WEAK", ["COMMONLY_USED"]),
    ("5841", "02-03-1997", "04-05-1998", "01-01-2001", "STRONG", []),
    ("020198", "02-01-1998", "04-05-1996", "01-01-2020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("123456", "01-01-1990", "02-02-1991", "03-03-1992", "WEAK", ["COMMONLY_USED"]),
    ("010298", "01-02-1998", "03-04-2000", "05-06-2010", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("040596", "02-03-1999", "04-05-1996", "01-01-2012", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("050615", "02-03-1999", "04-05-1996", "05-06-2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("888888", "02-02-2002", "04-04-2004", "06-06-2006", "STRONG", []),
    ("0198", "02-01-1998", "03-03-1996", "04-04-2014", "STRONG", []),
    ("2020", "20-02-1999", "01-01-2000", "01-01-2020", "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_ANNIVERSARY"]),
    ("111111", "11-11-1999", "11-11-1999", "11-11-1999", "WEAK", ["COMMONLY_USED"]),
    ("010199", "01-01-1999", "02-02-2002", "03-03-2003", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("010203", "01-01-1999", "02-02-2002", "03-03-2003", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("000000", "01-02-1990", "03-04-1990", "05-06-1990", "WEAK", ["COMMONLY_USED"]),
    ("070890", "07-08-1990", "01-01-2000", "01-01-2000", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("758391", "01-01-1999", "02-02-2002", "03-03-2003", "STRONG", [])
]

def main():
    for i, test in enumerate(tests, 1):
        run_test(i, *test)

# Allow calling directly or through import
if __name__ == "__main__":
    main()
