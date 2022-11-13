import tkinter as tk
import tkinter.ttk
import core.config
import core.download
import core.versions


def main():
    print(__file__+": load download page")

    def downmc():
        dotmc = core.config.read()[".mc"]

        core.download.download(download_as.get(), download_versions.get(), dotmc, int(core.config.read()["threads"]))
        print("Ok")

    def get_versions():
        vers = []
        if r.get() == 1:
            vers.append("release")
        if b.get() == 1:
            vers.append("snapshot")
        if o.get() == 1:
            vers.append("old_alpha")
        download_versions["values"] = core.versions.get_version_list(vers)

    def auto_fill_download_as(a):
        print(a)
        download_as.delete(0, tk.END)
        download_as.insert(0, download_versions.get())

    download_view = tk.ttk.Frame()

    download_versions_text = tk.ttk.Label(download_view, text="Game version:")
    download_versions_text.place(x=10, y=10)

    r = tk.IntVar()
    if_release = tk.ttk.Checkbutton(download_view, text="Release", variable=r)
    if_release.place(x=10, y=40)

    b = tk.IntVar()
    if_beta = tk.ttk.Checkbutton(download_view, text="Snapshot", variable=b)
    if_beta.place(x=80, y=40)

    o = tk.IntVar()
    if_old_alpha = tk.ttk.Checkbutton(download_view, text="Old Alpha", variable=o)
    if_old_alpha.place(x=160, y=40)

    download_versions = tk.ttk.Combobox(download_view, postcommand=get_versions)
    download_versions.bind('<<ComboboxSelected>>', auto_fill_download_as)
    download_versions.place(x=100, y=10)

    download_as_text = tk.ttk.Label(download_view, text="Download as:")
    download_as_text.place(x=10, y=70)

    download_as = tk.ttk.Entry(download_view)
    download_as.place(x=100, y=70)

    download_button = tk.ttk.Button(download_view, text="Download", command=downmc)
    download_button.place(x=10, y=200)

    return download_view
