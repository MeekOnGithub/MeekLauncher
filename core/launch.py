import json
import os
import uuid
import core.system


def getoptions(js: str):
    return js.replace("$", "")


def gethighoptions(js: list):
    temp = ""
    for i in js:
        if type(i) == str:
            temp += getoptions(i) + " "
    return temp


def addclasspath(rules: dict):
    localos = core.system.system()
    for i in rules:
        if i["action"] == "allow":
            if ("os" not in i) or (localos == i["os"]):
                return True
            else:
                return False

        elif i["action"] == "disallow":
            if ("os" not in i) or (localos == i["os"]):
                return False
            else:
                return True

        else:
            return -1


def launch(game_directory: str = ".minecraft", version_name: str = None, java: str = "java",
           auth_player_name: str = "player"):
    game_directory = os.path.realpath(game_directory)
    cps = []

    verpath = os.path.join(game_directory, "versions", version_name)
    libpath = os.path.join(verpath, "natives-windows-x86_64")
    jsonpath = os.path.join(verpath, version_name + ".json")
    jarpath = os.path.join(verpath, version_name + ".jar")
    logcfgpath = os.path.join(verpath, "log4j2.xml")

    if version_name is None:
        return 0
    if not (os.path.exists(game_directory) and os.path.exists(jsonpath)):
        return 1

    ver_json = json.load(open(jsonpath))

    temp = f"{java} -Dfile.encoding=GB18030 -Djava.library -Dminecraft.client.jar={jarpath} -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC " \
           f"-XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=16m -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -XX:-DontCompileHugeMethods " \
           f"-Xmn128m -Xmx3968m -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.rmi.server.useCodebaseOnly=true -Dcom.sun.jndi.rmi.object.trustURLCodebase=false -Dcom.sun.jndi.cosnaming.object.trustURLCodebase=false -Dlog4j2.formatMsgNoLookups=true -Dlog4j.configurationFile={logcfgpath} " \
           f"-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path={libpath} -Dminecraft.launcher.brand=FMCL -Dminecraft.launcher.version=0.2 -cp"
    for i in ver_json['libraries']:
        if "name" in i:
            if ("downloads" not in i) or ("classifiers" not in i["downloads"]):
                name = i["name"].split(":")  # <package>:<name>:<version>
                name[0] = name[0].replace(".", "/")
                p = name[0]
                n = name[1]
                v = name[2]
                rpath = os.path.join(game_directory, "libraries", p, n, v, n + "-" + v + ".jar")
                if ("rules" not in i) or (addclasspath(i["rules"])):
                    cps.append(os.path.realpath(rpath))  # <package>/<name>/<version>/<name>-<version>.jar

    assets_root = os.path.realpath(os.path.join(game_directory, "assets"))
    assets_index_name = ver_json["assetIndex"]["id"]
    auth_uuid = uuid.uuid4().hex
    auth_access_token = "0"
    user_type = "Legacy"
    version_type = '"First Minecraft Launcher Demo"'
    user_properties = "{}"
    auth_session = "{}"
    clientid = "0"
    auth_xuid = "0"
    game_assets = "resources"

    split = {"windows": ";", "osx": ":", "linux": ":", "unknown": "err"}
    cp = ""
    for i in cps:
        cp += i + split[core.system.system()]

    args = ""

    if "minecraftArguments" in ver_json:
        args = eval("f'" + getoptions(ver_json["minecraftArguments"]) + "'")

    elif "arguments" in ver_json and "game" in ver_json["arguments"]:
        args = eval("f'" + gethighoptions(ver_json["arguments"]["game"]) + "'")

    return f'{temp} {cp}{jarpath} {ver_json["mainClass"]} {args}'
