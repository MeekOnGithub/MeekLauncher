import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk

import view.themes.download
import view.themes.launch
import view.themes.setting


def main():
    root = tk.Tk()
    root.geometry('400x300')
    root.title('First Minecraft Launcher')
    root.resizable(0, 0)
    root.iconbitmap(os.path.dirname(__file__) + "/icon.ico")

    notebook = tk.ttk.Notebook(root)

    notebook.add(view.themes.launch.main(), text='Launch')
    notebook.add(view.themes.download.main(), text='Download')
    notebook.add(view.themes.setting.main(), text='Settings')

    notebook.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=True)

    root.mainloop()
