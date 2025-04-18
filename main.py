import tkinter as tk
from tkinter import messagebox

def on_button_click_1():
    messagebox.showinfo("Уведомление", "Вы нажали на первую кнопку")

def on_button_click_2():
    messagebox.showinfo("Уведомление", "Вы нажали на такую же кнопку")

# Создаем главное окно
root = tk.Tk()
root.title("Мое десктопное приложение")
root.geometry("300x200")  # Размер окна: ширина x высота

# Создаем первую кнопку
button1 = tk.Button(root, text="Нажми меня", command=on_button_click_1)
button1.pack(expand=True)

# Создаем вторую кнопку
button2 = tk.Button(root, text="И я такая же", command=on_button_click_2)
button2.pack(expand=True)

# Запускаем главный цикл приложения
root.mainloop()
