import json
import os
import os.path
import threading
import requests

import core.mkdir

paths = []
urls = []


def get_ver_jar_url(version: str):
    for i in requests.get("https://piston-meta.mojang.com/mc/game/version_manifest.json").json()['versions']:
        if i["id"] == version:
            return i["url"]


def get_task(version_name: str, version: str, mcpath: str, useBMCLAPI: bool):
    global paths, urls
    paths = []
    urls = []
    if useBMCLAPI:
        assets = "https://bmclapi2.bangbang93.com/assets"
        libraries = "https://bmclapi2.bangbang93.com/maven"
        forge = "https://bmclapi2.bangbang93.com/maven"
        fabricmeta = "https://bmclapi2.bangbang93.com/fabric-meta"
        fabricmaven = "https://bmclapi2.bangbang93.com/maven"
    else:
        assets = "https://resources.download.minecraft.net"
        libraries = "https://libraries.minecraft.net/"
        forge = "https://files.minecraftforge.net/maven"
        fabricmeta = "https://meta.fabricmc.net"
        fabricmaven = "https://maven.fabricmc.net"

    if os.path.exists(f"{mcpath}/versions/{version_name}"):
        print("Game is already installed. Please change a name.")
        return 0

    print("0 Create Game Folder")
    os.mkdir(f"{mcpath}/versions/{version_name}")

    print("1 Download version json")
    print(get_ver_jar_url(version))
    with open(f"{mcpath}/versions/{version_name}/{version_name}.json", "wb") as file:
        file.write(requests.get(get_ver_jar_url(version)).content)
    ver_json = json.load(open(f"{mcpath}/versions/{version_name}/{version_name}.json"))

    print("2 Download version jar")
    with open(f"{mcpath}/versions/{version_name}/{version_name}.jar", "wb") as file:
        file.write(requests.get(f"{ver_json['downloads']['client']['url']}").content)

    print("3 Download natives")
    for i in ver_json["libraries"]:
        try:
            urls.append(i["downloads"]["artifact"]["url"])
            paths.append(f"{mcpath}/libraries/{i['downloads']['artifact']['path']}")
        except KeyError:
            try:
                print("Special native!")
                urls.append(i["downloads"]["classifiers"]["natives-windows"]["url"])
                paths.append(f'{mcpath}/libraries/{i["downloads"]["classifiers"]["natives-windows"]["path"]}')

            except KeyError:
                print("Sprcial:", i)

    print("4 Download assets index")
    core.mkdir.make_dir(f"{mcpath}/assets/indexes")
    core.mkdir.make_dir(f"{mcpath}/assets/objects")
    with open(f"{mcpath}/assets/indexes/{ver_json['assetIndex']['id']}.json", "wb") as file:
        file.write(requests.get(ver_json['assetIndex']['url']).content)
    index_json = json.load(open(f"{mcpath}/assets/indexes/{ver_json['assetIndex']['id']}.json"))

    for i in index_json["objects"]:
        now_hash = index_json["objects"][i]["hash"]
        urls.append(f"{assets}/{now_hash[0:2]}/{now_hash}")
        paths.append(f"{mcpath}/assets/objects/{now_hash[0:2]}/{now_hash}")

    print("5 Download log4j2.xml file")
    core.mkdir.make_long_dir(f"{mcpath}\\versions\\{version_name}")
    urls.append(ver_json["logging"]["client"]["file"]["url"])
    paths.append(f"{mcpath}\\versions\\{version_name}\\log4j2.xml")

    print("6 Download natives jar")


def multprocessing_task(tasks: list, function, cores: int, join: bool = True):
    threads = []

    def _run():
        while threads:
            try:
                task = tasks.pop(0)
                function(task)
            except Exception:
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
    print(f"Downloading {url} to {path}")
    core.mkdir.make_long_dir(os.path.dirname(path))
    open(os.path.realpath(path), "wb").write(requests.get(url).content)
    print(f"Download {url} to {path} done.")


def download(ver_name: str, version: str, mcpath: str):
    get_task(ver_name, version, mcpath, False)
    tasks = []
    for i in range(len(urls)):
        tasks.append((urls[i], paths[i]))
    multprocessing_task(tasks, download_one, 100, True)
