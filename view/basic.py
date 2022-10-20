import os
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import core.config
import core.launch
import core.Muiti
import core.versions


def main():
    def start():
        conf = core.config.read()
        command = core.launch.launch(conf[".mc"], version.get(), conf["java"], conf["playername"])
        print(command)
        if command == 0:
            tk.messagebox.showerror("Null.")
        elif command == 1:
            tk.messagebox.showerror("Launch Failed!", "This version is not complete.")
        else:
            os.system(command)

    def downmc():
        dotmc = core.config.read()[".mc"]

        core.Muiti.download(versions.get(versions.curselection()), versions.get(versions.curselection()), dotmc)
        print("Ok")

    def conf():
        core.config.write(name.get(), dotmc.get(), java.get(), memory.get())

    def drop():
        version["values"] = core.versions.local_version(core.config.read()[".mc"])

    root = tk.Tk()
    root.geometry('400x300')
    root.title('First Minecraft Launcher')
    root.resizable(0, 0)

    notebook = tk.ttk.Notebook(root)

    # launch page #
    frame1 = tk.ttk.Frame()
    title = tk.ttk.Label(frame1, text="FMCL", font=("Arial", 20))
    title.place(x=20, y=5)
    about_this = tk.ttk.Label(frame1,
                              text="FMCL is a cracked Minecraft Launcher.\nThis is a preview version.\nJoin our KOOK: https://kook.top/9ccRg6 ",
                              font=("Arial", 12))
    about_this.place(x=20, y=35)
    launch = tk.ttk.Button(frame1, text="launch", width=20, command=start)
    launch.place(x=200, y=200)
    version = tk.ttk.Combobox(frame1, values=[0,1], postcommand=drop)
    version.place(x=20, y=200)

    # Download page #
    frame2 = tk.ttk.Frame()
    versions = tk.Listbox(frame2, selectmode=tk.SINGLE)
    versions.place(x=10, y=10)
    btn_ok = tk.ttk.Button(frame2, text="Download", command=downmc)
    btn_ok.place(x=10, y=200)

    # Setting page #
    frame3 = tk.ttk.Frame()
    tk.Label(frame3, text="java/javaw.exe: ").place(x=0, y=5)
    java = tk.ttk.Entry(frame3, show=None)
    java.place(x=90, y=5, width=200)
    btn_choosejava = tk.ttk.Button(frame3, text="Browse...")
    btn_choosejava.place(x=290, y=5)

    # minecraft路径模块
    tk.Label(frame3, text=".minecraft: ").place(x=0, y=30)
    dotmc = tk.ttk.Entry(frame3, show=None)
    dotmc.place(x=90, y=30, width=200)
    btn_choosejava = tk.ttk.Button(frame3, text="Browse...")
    btn_choosejava.place(x=290, y=30)

    # 玩家名模块
    tk.Label(frame3, text="playername:").place(x=0, y=55)
    name = tk.ttk.Entry(frame3, show=None)
    name.place(x=90, y=55, width=200)

    # 内存分配模块
    tk.Label(frame3, text="RAM given:").place(x=0, y=80)
    memory = tk.ttk.Entry(frame3, show=None)
    memory.place(x=90, y=80, width=200)

    btn_ok = tk.ttk.Button(frame3, text="OK", command=conf)

    btn_ok.place(x=160, y=180, width=40)

    # About page #
    frame4 = tk.ttk.Frame()
    about = tk.ttk.Label(frame4,
                         text="First Minecraft Launcher(FMCL) written by Sharll.\nDo not decompile and edit the code!",
                         font=("Arial", 12))
    about.place(x=5, y=5)

    notebook.add(frame1, text='Launch')
    notebook.add(frame2, text='Download')
    notebook.add(frame3, text='Settings')
    notebook.add(frame4, text='About')

    notebook.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=True)

    root.mainloop()
