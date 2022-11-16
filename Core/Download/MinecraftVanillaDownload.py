import json
import os
import os.path
import threading
import zipfile
import tkinter.messagebox
import Core.System.CoreSystemInformation

import requests

import Core.System.CoreMakeFolderTask

paths = []
urls = []
nativesjar = []


def get_ver_jar_url(version: str):
    for i in requests.get("https://piston-meta.mojang.com/mc/game/version_manifest.json").json()['versions']:
        if i["id"] == version:
            return i["url"]


def get_task(version_name: str, version: str, mcpath: str):
    assets = "https://resources.download.minecraft.net"

    global paths, urls, nativesjar
    paths = []
    urls = []
    nativesjar = []

    if os.path.exists(f"{mcpath}/versions/{version_name}"):
        tkinter.messagebox.showinfo("Info", "The folder is exist. Launch fixing mode.")

    # create game folder
    Core.System.CoreMakeFolderTask.make_long_dir(f"{mcpath}/versions/{version_name}")

    # download version json
    with open(f"{mcpath}/versions/{version_name}/{version_name}.json", "wb") as file:
        file.write(requests.get(get_ver_jar_url(version)).content)
    ver_json = json.load(open(f"{mcpath}/versions/{version_name}/{version_name}.json"))

    # add version.jar to task
    urls.append(f"{ver_json['downloads']['client']['url']}")
    paths.append(f"{mcpath}/versions/{version_name}/{version_name}.jar")

    # natives
    for i in ver_json["libraries"]:

        if "artifact" in i["downloads"]:
            urls.append(i["downloads"]["artifact"]["url"])
            paths.append(f'{mcpath}/libraries/{i["downloads"]["artifact"]["path"]}')

        if ("classifiers" in i["downloads"]) and "natives-"+ Core.System.CoreSystemInformation.system() in i["downloads"]["classifiers"]:
            print(i)
            urls.append(i["downloads"]["classifiers"]["natives-windows"]["url"])
            paths.append(f'{mcpath}/libraries/{i["downloads"]["classifiers"]["natives-windows"]["path"]}')
            nativesjar.append(f'{mcpath}/libraries/{i["downloads"]["classifiers"]["natives-windows"]["path"]}')
        # if "extract" in i:
        #     print(i)

    # assets
    Core.System.CoreMakeFolderTask.make_dir(f"{mcpath}/assets/indexes")
    Core.System.CoreMakeFolderTask.make_dir(f"{mcpath}/assets/objects")
    with open(f"{mcpath}/assets/indexes/{ver_json['assetIndex']['id']}.json", "wb") as file:
        file.write(requests.get(ver_json['assetIndex']['url']).content)
    index_json = json.load(open(f"{mcpath}/assets/indexes/{ver_json['assetIndex']['id']}.json"))
    for i in index_json["objects"]:
        now_hash = index_json["objects"][i]["hash"]
        urls.append(f"{assets}/{now_hash[0:2]}/{now_hash}")
        paths.append(f"{mcpath}/assets/objects/{now_hash[0:2]}/{now_hash}")

    # log4j config
    Core.System.CoreMakeFolderTask.make_long_dir(f"{mcpath}\\versions\\{version_name}")
    urls.append(ver_json["logging"]["client"]["file"]["url"])
    paths.append(f"{mcpath}\\versions\\{version_name}\\log4j2.xml")


def multprocessing_task(tasks: list, function, cores: int, join: bool = True):
    threads = []

    def _run():
        while threads:
            try:
                task = tasks.pop(0)
                function(task)
            except threading.ExceptHookArgs:
                break

    for i in range(cores + 1):
        thread = threading.Thread(target=_run)
        thread.start()
        threads.append(thread)

    if join:
        for thread in threads:
            thread.join()


def download_one(i):
    url = i[0]
    path = i[1]
    Core.System.CoreMakeFolderTask.make_long_dir(os.path.dirname(path))
    open(os.path.realpath(path), "wb").write(requests.get(url).content)


def download(ver_name: str, version: str, mcpath: str, threads: int):
    get_task(ver_name, version, mcpath)
    tasks = []
    for i in range(len(urls)):
        tasks.append((urls[i], paths[i]))
    multprocessing_task(tasks, download_one, threads, True)

    for i in nativesjar:
        print(i)
        jar = os.path.realpath(i)
        Core.System.CoreMakeFolderTask.make_long_dir(os.path.realpath(
            f'{os.path.realpath(mcpath)}/versions/{ver_name}/natives-windows-x86_64'))
        zip_file = zipfile.ZipFile(jar)
        for names in zip_file.namelist():
            zip_file.extract(names, os.path.realpath(
                f'{os.path.realpath(mcpath)}/versions/{ver_name}/natives-windows-x86_64'))
