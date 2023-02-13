import tkinter as tk


def count():
    global count_value
    count_value += 1
    count_label.config(text=f"Total: {count_value}")

count_value = 0

root = tk.Tk()
root.title("Counter")

count_label = tk.Label(root, text=f"Total: {count_value}")
count_label.grid(row=0, column=0, padx=5, pady=5)

count_button = tk.Button(root, text="+1", command=count)
count_button.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
