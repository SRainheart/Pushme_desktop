import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Уведомление", "Вы нажали на кнопку")

# Создаем главное окно
root = tk.Tk()
root.title("Мое десктопное приложение")
root.geometry("300x200")  # Размер окна: ширина x высота

# Создаем кнопку по центру
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack(expand=True)

# Запускаем главный цикл приложения
root.mainloop()
