import tkinter as tk
from tkinter import messagebox
from part_d_6digit_support import evaluate_mpin

# --- Check function ---
def check_mpin():
    mpin = mpin_entry.get().strip()
    dob = dob_entry.get().strip()
    spouse_dob = spouse_dob_entry.get().strip()
    anniversary = anniversary_entry.get().strip()

    if not mpin.isdigit() or len(mpin) not in [4, 6]:
        messagebox.showerror("Invalid MPIN", "MPIN must be a 4 or 6-digit number.")
        return
    if dob and not valid_date(dob):
        messagebox.showerror("Invalid Date", "Please enter your DOB in dd-mm-yyyy format.")
        return
    if spouse_dob and not valid_date(spouse_dob):
        messagebox.showerror("Invalid Date", "Spouse DOB must be in dd-mm-yyyy format.")
        return
    if anniversary and not valid_date(anniversary):
        messagebox.showerror("Invalid Date", "Anniversary must be in dd-mm-yyyy format.")
        return

    strength, reasons = evaluate_mpin(mpin, dob, spouse_dob, anniversary)
    if strength == "STRONG":
        result_label.config(fg="green")
    else:
        result_label.config(fg="red")

    result_text.set(f"🛡️ Strength: {strength}\n📌 Reasons: {', '.join(reasons) if reasons else 'None'}")


# --- Helper: date format validation ---
def valid_date(d):
    parts = d.split("-")
    return len(parts) == 3 and all(p.isdigit() for p in parts) and len(parts[0]) == 2 and len(parts[1]) == 2 and len(parts[2]) == 4


# --- Reset all fields ---
def reset_fields():
    mpin_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    spouse_dob_entry.delete(0, tk.END)
    anniversary_entry.delete(0, tk.END)
    result_text.set("")
    result_label.config(fg="black")


# --- Exit Confirmation ---
def on_closing():
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()


# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 MPIN Security Evaluator")
root.geometry("450x330")
root.resizable(False, False)


# --- Form Layout ---
frame = tk.Frame(root, padx=20, pady=10)
frame.pack()

tk.Label(frame, text="MPIN (4 or 6 digits):").grid(row=0, column=0, sticky="w", pady=5)
tk.Label(frame, text="Your DOB (dd-mm-yyyy):").grid(row=1, column=0, sticky="w", pady=5)
tk.Label(frame, text="Spouse DOB [Optional]:").grid(row=2, column=0, sticky="w", pady=5)
tk.Label(frame, text="Anniversary [Optional]:").grid(row=3, column=0, sticky="w", pady=5)

mpin_entry = tk.Entry(frame, width=25)
dob_entry = tk.Entry(frame, width=25)
spouse_dob_entry = tk.Entry(frame, width=25)
anniversary_entry = tk.Entry(frame, width=25)

mpin_entry.grid(row=0, column=1)
dob_entry.grid(row=1, column=1)
spouse_dob_entry.grid(row=2, column=1)
anniversary_entry.grid(row=3, column=1)

tk.Button(frame, text="✅ Check MPIN", command=check_mpin, bg="#4CAF50", fg="white", width=15).grid(row=4, column=0, pady=15)
tk.Button(frame, text="🔁 Reset", command=reset_fields, width=15).grid(row=4, column=1)


# --- Result Display ---
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 10), wraplength=400)
result_label.pack(pady=5)


# --- Exit Hook ---
root.protocol("WM_DELETE_WINDOW", on_closing)

# --- Start ---
root.mainloop()
