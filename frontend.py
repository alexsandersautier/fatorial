from backend import *
from tkinter import *
def calculate():
    lbl_result.config(text="")
    number = input_number.get() 
    result = calculate_fatorial(number, True)
    result = f"A fatorial do número {str(number)} é {str(result)}"
    lbl_result.config(text=result)
    input_number.delete(0, END)

root = Tk()
root.title("Calculadora de fatorial")
root.geometry("250x200")
lbl_number = Label(root, text="Digite um número: ").grid(row=0, column=0)
input_number = Entry(root)
input_number.grid(row=0, column=1)
btn_calculate = Button(root, text="Calcular", command=calculate).grid(row=1, columnspan=2)
lbl_result = Label(root, text="")
lbl_result.grid(row=2, columnspan=2)

root.mainloop()    
