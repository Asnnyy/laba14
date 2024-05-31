import tkinter as tk
from tkinter import messagebox
bg_c = 'ivory'
color1 = 'PaleTurquoise4'
color2 = 'seashell'
f_c = 'black'
f1 = ('Arial', 25, 'bold')
food = {
    'Мексика': ['Tres Amigos', 'Tequila-Boom', 'Mapuche'],
    'Россия': ['Чеховъ', 'Трактир Хлебниковъ', 'Katusha'],
    'Италия': ['Мука', 'GooseGoose', 'Amo cucinare'],
    'Индия': ['Намасте', 'Oh! Mumbai', 'My Asiatique'],
    'Франция': ['Bistrot Le Moujik', 'Legran', 'Julia Child'],
    'Китай': ['Sintoho', 'Jack and Chan', 'TopEr'],
    'Япония': ['Ярумэн', 'MOJO', 'Gills'],
    'Грузия': ['Хочу харчо', 'Мамалыга', 'Хачапури и Вино'],
    'Испания': ['Барселона', 'Pinch', 'Las Torres'],
    'Корея': ['Кореана', 'Малатан', 'See Asia'],
    'Тайланд': ['Thai Fun', 'Chang Cafe', 'Бао Мочи'],
    'Израиль': ['Saviv', 'Lafa Lafa', 'Leila by Ezo']
}
class WorldCuisines:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.title("Кухни мира")
        self.root.config(bg = bg_c)
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Введите страну", foreground = color1, background = bg_c, font = f1)
        self.label.pack(pady=10)
        self.country_entry = tk.Entry(self.root, background = color2, foreground = f_c)
        self.country_entry.pack(pady=5)
        self.search_button = tk.Button(self.root, background = bg_c, text="Показать рестораны", command=self.show_rest)
        self.search_button.pack(pady=7)
        self.result_label = tk.Label(self.root, background = bg_c, foreground = f_c, text="", wraplength=350)
        self.result_label.pack(pady=10)
    def show_rest(self):
        country = self.country_entry.get().strip()
        rest = food.get(country)
        if rest:
            self.result_label.configure(text=f"Популярные рестораны страны {country} в Санкт-Петербурге:\n" + "\n".join(rest))
        else:
            messagebox.showerror("Ошибка!", f"Не нашли рестораны страны {country}")
if __name__ == "__main__":
    root = tk.Tk()
    okno = WorldCuisines(root)
    root.mainloop()
