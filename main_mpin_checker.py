# main_mpin_checker.py
# Enhanced version with menu + loop support

from part_d_6digit_support import evaluate_mpin
import test_mpin_checker

def run_manual_mode():
    while True:
        try:
            print("\n🔐 MPIN Security Check")
            print("-----------------------")
            mpin = input("Enter your MPIN (4 or 6 digits): ").strip()

            if len(mpin) not in [4, 6] or not mpin.isdigit():
                raise ValueError("MPIN must be a 4 or 6-digit number.")

            dob_self = input("Enter your Date of Birth (dd-mm-yyyy): ").strip()
            dob_spouse = input("Enter spouse's DOB (dd-mm-yyyy): ").strip()
            anniversary = input("Enter wedding anniversary (dd-mm-yyyy): ").strip()

            strength, reasons = evaluate_mpin(mpin, dob_self, dob_spouse, anniversary)

            print("\n🛡️ Strength:", strength)
            print("📌 Reasons :", reasons if reasons else "[]")

        except ValueError as ve:
            print("❌ Input Error:", ve)
        except Exception as e:
            print("❌ Unexpected Error:", e)

        # Ask to repeat
        again = input("\nDo you want to check another MPIN? (y/n): ").strip().lower()
        if again != 'y':
            break


def run_menu():
    while True:
        print("\n===== MPIN Evaluator Menu =====")
        print("1. Manual Mode (Enter MPIN and Dates)")
        print("2. Run All Test Cases")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ").strip()

        if choice == '1':
            run_manual_mode()
        elif choice == '2':
            print("\n🧪 Running All Test Cases...\n")
            test_mpin_checker.main()
        elif choice == '3':
            print("👋 Exiting. Thank you!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    run_menu()
