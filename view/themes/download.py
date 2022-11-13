import tkinter as tk
import tkinter.ttk
import core.config
import core.download
import core.versions


def main():
    print("load download page")

    def downmc():
        """
        This function is used to download a game.
        """
        dotmc = core.config.read()[".mc"]

        core.download.download(download_as.get(), download_versions.get(), dotmc, int(core.config.read()["threads"]))
        print("Ok")

    def get_versions():
        download_versions["values"] = core.versions.get_version_list("release")

    def auto_fill_download_as(a):
        print(a)
        download_as.delete(0, tk.END)
        download_as.insert(0, download_versions.get())

    download_view = tk.ttk.Frame()
    download_versions_text = tk.ttk.Label(download_view, text="Game version:")
    download_versions_text.place(x=10, y=10)
    download_versions = tk.ttk.Combobox(download_view, postcommand=get_versions)
    download_versions.bind('<<ComboboxSelected>>', auto_fill_download_as)
    download_versions.place(x=100, y=10)
    download_as_text = tk.ttk.Label(download_view, text="Download as:")
    download_as_text.place(x=10, y=50)
    download_as = tk.ttk.Entry(download_view)
    download_as.place(x=100, y=50)
    download_button = tk.ttk.Button(download_view, text="Download", command=downmc)
    download_button.place(x=10, y=200)

    return download_view
