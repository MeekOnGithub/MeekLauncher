import os
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import core.config
import core.launch
import core.Muiti
import core.versions
import core.mkdir
import tkinter.filedialog


def main():
    def start():
        """
        This function is used to launch a game,
        """
        command = core.launch.launch(core.config.read()[".mc"], launch_version.get(), core.config.read()["java"], core.config.read()["playername"])
        print(command)
        if command == 0:
            tk.messagebox.showerror("Null.")
        elif command == 1:
            tk.messagebox.showerror("Launch Failed!", "This version is not complete.")
        else:
            os.system(command)

    def downmc():
        """
        This function is used to download a game.
        """
        dotmc = core.config.read()[".mc"]

        core.Muiti.download(download_as.get(), download_versions.get(), dotmc)
        print("Ok")

    def conf():
        # simple write config
        core.config.write(setting_playername.get(), setting_dotmc.get(), setting_java.get(), setting_ram_give.get())

    def drop():
        # refresh version choose
        launch_version["values"] = core.versions.local_version(core.config.read()[".mc"])

    def refresh():
        setting_java.delete(0, "end")
        setting_java.insert(0, core.config.read()["java"])
        setting_dotmc.delete(0, "end")
        setting_dotmc.insert(0, core.config.read()[".mc"])
        setting_playername.delete(0, "end")
        setting_playername.insert(0, core.config.read()["playername"])
        setting_ram_give.delete(0, "end")
        setting_ram_give.insert(0, core.config.read()["ram"])

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

    def get_versions():
        download_versions["values"] = core.versions.get_version_list("release")

    root = tk.Tk()
    root.geometry('400x300')
    root.title('First Minecraft Launcher')
    root.resizable(0, 0)
    root.iconbitmap(os.path.dirname(__file__)+"/icon.ico")

    notebook = tk.ttk.Notebook(root)

    # launch page #
    launch_view = tk.ttk.Frame()
    launch_title = tk.ttk.Label(launch_view, text="FMCL", font=("Arial", 20))
    launch_title.place(x=20, y=5)
    launch_about = tk.ttk.Label(launch_view,
                                text="FMCL is a cracked Minecraft Launcher.\nThis is a preview version.\nJoin our KOOK: https://kook.top/9ccRg6 ",
                                font=("Arial", 12))
    launch_about.place(x=20, y=35)
    launch_launch = tk.ttk.Button(launch_view, text="launch", width=20, command=start)
    launch_launch.place(x=200, y=200)
    launch_version = tk.ttk.Combobox(launch_view, postcommand=drop)
    launch_version.place(x=20, y=200)

    download_view = tk.ttk.Frame()
    download_versions = tk.ttk.Combobox(download_view, postcommand=get_versions)
    download_versions.place(x=10, y=10)
    download_as = tk.ttk.Entry(download_view)
    download_as.place(x=10, y=50)
    download_button = tk.ttk.Button(download_view, text="Download", command=downmc)
    download_button.place(x=10, y=200)

    # Setting page #
    setting_view = tk.ttk.Frame()
    tk.Label(setting_view, text="java/javaw.exe: ").place(x=0, y=5)
    setting_java = tk.ttk.Entry(setting_view, show=None)
    setting_java.place(x=90, y=5, width=200)
    setting_choose_dmc_button = tk.ttk.Button(setting_view, text="Browse...", command=choosefile)
    setting_choose_dmc_button.place(x=290, y=5)

    # minecraft路径模块
    tk.Label(setting_view, text=".minecraft: ").place(x=0, y=30)
    setting_dotmc = tk.ttk.Entry(setting_view, show=None)
    setting_dotmc.place(x=90, y=30, width=200)
    setting_choose_dmc_button = tk.ttk.Button(setting_view, text="Browse...", command=choosefolder)
    setting_choose_dmc_button.place(x=290, y=30)

    # 玩家名模块
    tk.Label(setting_view, text="playername:").place(x=0, y=55)
    setting_playername = tk.ttk.Entry(setting_view, show=None)
    setting_playername.place(x=90, y=55, width=200)

    # 内存分配模块
    tk.Label(setting_view, text="RAM given:").place(x=0, y=80)
    setting_ram_give = tk.ttk.Entry(setting_view, show=None)
    setting_ram_give.place(x=90, y=80, width=200)

    setting_save_button = tk.ttk.Button(setting_view, text="Save", command=conf)
    setting_refresh_button = tk.ttk.Button(setting_view, text="Refresh", command=refresh)

    setting_refresh_button.place(x=100, y=180, width=80)
    setting_save_button.place(x=180, y=180, width=80)

    # About page #
    about_view = tk.ttk.Frame()
    about_about = tk.ttk.Label(about_view,
                               text="First Minecraft Launcher(FMCL) written by Sharll.\n"
                                    "Do not decompile and edit the code!",
                               font=("Arial", 12))
    about_about.place(x=5, y=5)

    notebook.add(launch_view, text='Launch')
    notebook.add(download_view, text='Download')
    notebook.add(setting_view, text='Settings')
    notebook.add(about_view, text='About')

    notebook.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=True)

    refresh()

    root.mainloop()


if __name__ == "__main__":
    make = core.mkdir.Files()
    make.make_mc_dir(".")
    if not os.path.exists("config.json"):
        core.config.write()
    print(core.config.read())
    main()
