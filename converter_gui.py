import tkinter as tk

def to_binary(decimal_number):
    return bin(decimal_number)[2:]

def to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

def to_octal(decimal_number):
    return oct(decimal_number)[2:] 

def to_bcd(decimal_number):
    bcd_nibbles = []
    for digit in str(decimal_number):
        four_bit = bin(int(digit))[2:].zfill(4)
        bcd_nibbles.append(four_bit)
    return ''.join(bcd_nibbles)

def convert_number():
    user_input = entry_box.get().strip()

    if not user_input.isdigit():
        result_label.config(text="Please enter a valid positive number.")
        return

    decimal_number = int(user_input)
    binary_result = to_binary(decimal_number)
    hexadecimal_result = to_hexadecimal(decimal_number)
    octal_result = to_octal(decimal_number)
    bcd_result = to_bcd(decimal_number)

    result_text = (
        f"Binary: {binary_result}\n"
        f"Hexadecimal: {hexadecimal_result}\n"
        f"Octal: {octal_result}\n"
        f"BCD: {bcd_result}"
    )
    result_label.config(text=result_text)

window = tk.Tk()
window.title("Number Base & BCD Converter")
window.geometry("420x320")
window.configure(bg="#0d1117")

tk.Label(
    window,
    text="Enter a Decimal Number",
    font=("Segoe UI", 12, "bold"),
    bg="#0d1117",
    fg="#e6edf3",
).pack(pady=(22, 8))

entry_box = tk.Entry(
    window,
    font=("Consolas", 14),
    justify="center",
    bg="#161b22",
    fg="#ffffff",
    insertbackground="#58a6ff", 
    bd=0,
    highlightthickness=2,  
    highlightbackground="#30363d",  
    highlightcolor="#58a6ff",  
)
entry_box.pack(pady=5, ipadx=15, ipady=8)
entry_box.focus()

convert_btn = tk.Button(
    window,
    text="Convert",
    font=("Segoe UI", 11, "bold"),
    bg="#236786",
    fg="#ffffff",
    activebackground="#2e95a0",
    activeforeground="#ffffff",
    bd=0,
    cursor="hand2",
    command=convert_number,
)
convert_btn.pack(pady=15, ipadx=25, ipady=6)

result_label = tk.Label(
    window,
    text="Result will appear here...",
    font=("Consolas", 11),
    justify="left",
    bg="#161b22",
    fg="#8b949e",
    padx=20,
    pady=15,
)
result_label.pack(pady=5, fill="x", padx=30)

window.mainloop()