import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import tkinter.font

import View.Themes.DownloadPage
import View.Themes.LaunchPage
import View.Themes.SettingPage
import View.Themes.AccountManagePage
import View.Themes.AboutPage


def main():
    print("Using FMCL GUI core 1.0 by Sharll.")
    root = tk.Tk()
    root.geometry('400x300')
    root.title('First Minecraft Launcher')
    root.resizable(0, 0)
    root.iconbitmap(os.path.join(os.path.dirname(__file__), "Resources", "icon.ico"))

    notebook = tk.ttk.Notebook(root)

    img1 = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "Resources", "Launch.png"))
    notebook.add(View.Themes.LaunchPage.main(), text='Launch', image=img1, compound="left")
    notebook.add(View.Themes.DownloadPage.main(), text='Download')
    notebook.add(View.Themes.SettingPage.main(), text='Settings')
    notebook.add(View.Themes.AccountManagePage.main(), text="Accounts")
    notebook.add(View.Themes.AboutPage.main(), text="About")

    notebook.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

    root.mainloop()
