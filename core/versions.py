import os

import requests


def add(o):
    if " " in o:
        return '"'+o+'"'
    return o


def get_version_list(version_type: str):
    versions = []
    for i in requests.get("https://bmclapi2.bangbang93.com/mc/game/version_manifest.json").json()['versions']:
        if i["type"] == version_type:
            versions.append(i["id"])
    return versions


def local_version(mcpath):
    versions = []
    for i in os.listdir(os.path.join(mcpath, "versions")):
        if os.path.exists(os.path.join(mcpath, "versions", i, f"{i}.jar")) and os.path.exists(os.path.join(mcpath, "versions", i, f"{i}.json")):
            versions.append(i)
    return versions


def java_versions():
    versions = ["java"]
    for i in os.getenv("path").split(";"):
        if os.path.exists(os.path.join(i, "java.exe")):
            versions.append('"' + os.path.join(i, "java.exe") + '"')
        elif os.path.exists(os.path.join(i, "javaw.exe")):
            versions.append('"' + os.path.join(i, "javaw.exe") + '"')

        if os.path.exists(os.path.join(i, "bin", "java.exe")):
            versions.append('"' + os.path.join(i, "bin", "java.exe") + '"')
        elif os.path.exists(os.path.join(i, "bin", "javaw.exe")):
            versions.append('"' + os.path.join(i, "bin", "javaw.exe") + '"')

    return versions


print(java_versions())
