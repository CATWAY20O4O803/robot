import tkinter as tk
from tkinter import ttk

class SliderEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Multiple Sliders with Entry Example")

        self.sliders = []
        self.entries = []
        self.labels = []
        self.entry_vars = []

        for i in range(12):
            self.create_slider_entry_pair(i)

        # button
        self.button = ttk.Button(self.root, text="storage", command=self.on_button_click)
        self.button.grid(row=12, column=0, columnspan=3, pady=10)

    def create_slider_entry_pair(self, index):
        # 造 slider
        slider = ttk.Scale(self.root, from_=0, to=255, orient='horizontal', command=lambda event, idx=index: self.on_slider_change(event, idx))
        slider.grid(row=index, column=0, padx=10, pady=5)
        self.sliders.append(slider)

        # 造輸入框
        entry_var = tk.StringVar()
        entry_var.trace("w", lambda name, index, mode, idx=index: self.on_entry_change(idx))
        entry = ttk.Entry(self.root, textvariable=entry_var)
        entry.grid(row=index, column=1, padx=10, pady=5)
        self.entries.append(entry)
        self.entry_vars.append(entry_var)

        # Ui
        label = ttk.Label(self.root, text=f"Slider {index + 1} Value: 0")
        label.grid(row=index, column=2, padx=10, pady=5)
        self.labels.append(label)

        # 初始
        entry_var.set(slider.get())

    def on_slider_change(self, event, index):
        value = int(self.sliders[index].get())
        self.entry_vars[index].set(value)
        self.labels[index].config(text=f"Slider {index + 1} Value: {value}")

    def on_entry_change(self, index):
        try:
            value = int(self.entry_vars[index].get())
            self.sliders[index].set(value)
            self.labels[index].config(text=f"Slider {index + 1} Value: {value}")
        except ValueError:
            pass

    def on_button_click(self):
        values = [slider.get() for slider in self.sliders]
        print("Last state:", values)

if __name__ == '__main__':
    root = tk.Tk()
    app = SliderEntryApp(root)
    root.mainloop()
