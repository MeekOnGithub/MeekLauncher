import os

import requests
import json


def get_version_list(type: str):
    versions = {}
    for i in requests.get("https://bmclapi2.bangbang93.com/mc/game/version_manifest.json").json()['versions']:
        if i["type"] == type:
            versions[i["id"]] = i["url"]
    return versions


def local_version(mcpath):
    versions = []
    for i in os.listdir(f"{mcpath}\\versions"):
        if os.path.exists(f"{mcpath}\\versions\\{i}\\{i}.jar") and os.path.exists(f"{mcpath}\\versions\\{i}\\{i}.json"):
            versions.append(i)
    return versions



