import tkinter as tk
import tkinter.ttk
import tkinter.filedialog
import core.config


def main():
    print("load setting page")

    def conf():
        # simple write config
        core.config.write(setting_playername.get(), setting_dotmc.get(), setting_java.get(), setting_ram_give.get(),
                          int(setting_threads.get()))

    def refresh():
        setting_java.delete(0, "end")
        setting_java.insert(0, core.config.read()["java"])
        setting_dotmc.delete(0, "end")
        setting_dotmc.insert(0, core.config.read()[".mc"])
        setting_playername.delete(0, "end")
        setting_playername.insert(0, core.config.read()["playername"])
        setting_ram_give.delete(0, "end")
        setting_ram_give.insert(0, core.config.read()["ram"])
        setting_threads.delete(0, "end")
        setting_threads.insert(0, core.config.read()["threads"])

    def choosefile():
        jpath = tk.filedialog.askopenfilenames(filetypes=[('java/javaw程序', '.exe')])
        if jpath:
            setting_java.delete(0, "end")
            setting_java.insert(0, '"' + jpath[0] + '"')

    def choosefolder():
        dpath = tk.filedialog.askdirectory()
        if dpath:
            setting_dotmc.delete(0, "end")
            setting_dotmc.insert(0, dpath)

    # Setting page #
    setting_view = tk.ttk.Frame()
    tk.Label(setting_view, text="java/javaw.exe: ").place(x=0, y=5)
    setting_java = tk.ttk.Entry(setting_view, show=None)
    setting_java.place(x=90, y=5, width=200)
    setting_choose_dmc_button = tk.ttk.Button(setting_view, text="Browse...", command=choosefile)
    setting_choose_dmc_button.place(x=290, y=2)

    # minecraft路径模块
    tk.Label(setting_view, text=".minecraft: ").place(x=0, y=30)
    setting_dotmc = tk.ttk.Entry(setting_view, show=None)
    setting_dotmc.place(x=90, y=30, width=200)
    setting_choose_dmc_button = tk.ttk.Button(setting_view, text="Browse...", command=choosefolder)
    setting_choose_dmc_button.place(x=290, y=27)

    # 玩家名模块
    tk.Label(setting_view, text="playername:").place(x=0, y=55)
    setting_playername = tk.ttk.Entry(setting_view, show=None)
    setting_playername.place(x=90, y=55, width=200)

    # 内存分配模块
    tk.Label(setting_view, text="RAM given:").place(x=0, y=80)
    setting_ram_give = tk.ttk.Entry(setting_view, show=None)
    setting_ram_give.place(x=90, y=80, width=200)

    tk.Label(setting_view, text="Download threads max count:").place(x=0, y=105)
    setting_threads = tk.ttk.Entry(setting_view, show=None)
    setting_threads.place(x=180, y=105, width=105)

    setting_save_button = tk.ttk.Button(setting_view, text="Save", command=conf)
    setting_refresh_button = tk.ttk.Button(setting_view, text="Refresh", command=refresh)

    setting_refresh_button.place(x=100, y=180, width=80)
    setting_save_button.place(x=180, y=180, width=80)

    refresh()

    return setting_view
