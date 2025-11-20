import tkinter as tk


def show_color():
    global r
    global g
    global b
    try:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError

        root.configure(bg=f"#{r:02x}{g:02x}{b:02x}")
    except:
        root.configure(bg="red")


def invert_color():
    global r
    global g
    global b
    r = 255 - r
    g = 255 - g
    b = 255 - b
    root.configure(bg=f"#{r:02x}{g:02x}{b:02x}")


# початкові значення
r = g = b = 255

root = tk.Tk()
root.title("RGB Reverse")
root.geometry("500x500")

# === РЯДОК З ПОЛЯМИ RGB (ГОРИЗОНТАЛЬНО) ===
inputs_frame = tk.Frame(root)
inputs_frame.pack(pady=20)

label_r = tk.Label(inputs_frame, text="R:")
label_r.pack(side="left", padx=5)
entry_r = tk.Entry(inputs_frame, width=5)
entry_r.pack(side="left", padx=5)

label_g = tk.Label(inputs_frame, text="G:")
label_g.pack(side="left", padx=5)
entry_g = tk.Entry(inputs_frame, width=5)
entry_g.pack(side="left", padx=5)

label_b = tk.Label(inputs_frame, text="B:")
label_b.pack(side="left", padx=5)
entry_b = tk.Entry(inputs_frame, width=5)
entry_b.pack(side="left", padx=5)

# === РЯДОК З КНОПКАМИ (ГОРИЗОНТАЛЬНО) ===
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

btn_show = tk.Button(buttons_frame, text="Show color", command=show_color)
btn_show.pack(side="left", padx=10)

btn_reverse = tk.Button(buttons_frame, text="Reverse", command=invert_color)
btn_reverse.pack(side="left", padx=10)

root.mainloop()