import customtkinter

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("400x500")
app.title("calculadora ctk")
app.resizable(False, False)

font = ("arial", 30)


frame = customtkinter.CTkFrame(master=app)
frame.pack(fill="both", expand=True)

entry = customtkinter.CTkEntry(frame, state="normal", width=400, height=70, corner_radius=0, font=font)
entry.grid(row=0, column=0, columnspan=4)
def button_click(value):
    current = entry.get()
    entry.delete(0, customtkinter.END)
    entry.insert(customtkinter.END, current + value)

def button_clear():
    entry.delete(0, customtkinter.END)

def button_equal():
    try:
        result = eval(entry.get())  # Avalia a expressão matemática
        entry.delete(0, customtkinter.END)
        entry.insert(customtkinter.END, result)
    except Exception as e:
        entry.delete(0, customtkinter.END)
        entry.insert(customtkinter.END, "Erro")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

especiais = ["-", "+", "*", "/"]

for i in range(5):
    frame.grid_rowconfigure(i, weight=1, uniform="equal")
for i in range(4):
    frame.grid_columnconfigure(i, weight=1, uniform="equal")

# Criando os botões e adicionando-os na grade
for (text, row, col) in buttons:
    if text == '=':
        btn = customtkinter.CTkButton(frame, text=text, font=('Arial', 20), command=button_equal, fg_color="#4CAF50", hover_color="#3A9D23")

    elif text in especiais:
        btn = customtkinter.CTkButton(frame, text=text, font=('Arial', 20), command=lambda value=text: button_click(value), fg_color="#4CAF50", hover_color="#3A9D23")

    elif text == 'C':
        btn = customtkinter.CTkButton(frame, text=text, font=('Arial', 20), command=button_clear, fg_color="#F44336", hover_color="#e53935")
    else:
        btn = customtkinter.CTkButton(frame, text=text, font=('Arial', 20), command=lambda value=text: button_click(value))
    
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

app.mainloop()