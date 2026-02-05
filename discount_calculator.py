import tkinter as tk

def calculate_discount():
    price = float(entry_price.get())
    discount = float(entry_discount.get())
    quantity = int(entry_quantity.get())

    subtotal = price * quantity
    final_price = subtotal - (subtotal * (discount / 100))

    label_result.config(text=f"Final Price: Rp {final_price:.2f}")

root = tk.Tk()
root.title("Discount Calculator")

tk.Label(root, text="Original Price:").pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack(pady=5)

tk.Label(root, text="Quantity:").pack(pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.pack(pady=5)

tk.Label(root, text="Discount (%):").pack(pady=5)
entry_discount = tk.Entry(root)
entry_discount.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_discount).pack(pady=20)

label_result = tk.Label(root, text="Final Price: Rp 0.00")
label_result.pack(pady=10)

root.mainloop()
