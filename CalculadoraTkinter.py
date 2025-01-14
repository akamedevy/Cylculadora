import tkinter as tk
from tkinter import messagebox  # Importa a função para criar o popup

# Função que adiciona o número ou operador à tela
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Limpa a tela
    entry.insert(tk.END, current + value)

# Função que limpa a tela
def button_clear():
    entry.delete(0, tk.END)

# Função que calcula o resultado e mostra em um popup
def button_equal():
    try:
        result = eval(entry.get())  # Avalia a expressão matemática
        entry.delete(0, tk.END)
        # entry.insert(tk.END, result)
        
        # Exibe o resultado em um popup
        messagebox.showinfo("Resultado", f"O resultado é: {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")
        messagebox.showerror("Erro", "Ocorreu um erro na expressão!")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Configuração da tela (entrada de texto)
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda value=text: button_click(value))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
