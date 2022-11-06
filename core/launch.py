import json
import os
import uuid


def getoptions(js: str):
    return js.replace("$", "")


def gethighoptions(js: list):
    temp = ""
    for i in js:
        if type(i) == str:
            temp += getoptions(i) + " "
    return temp


def launch(game_directory: str = ".minecraft", version_name: str = None, java: str = "java",
           auth_player_name: str = "player"):
    game_directory = os.path.realpath(game_directory)
    cps = []
    if version_name is None:
        return 0
    if not (os.path.exists(game_directory) and os.path.exists(
            f"{game_directory}/versions/{version_name}/{version_name}.json")):
        return 1
    ver_json = json.load(open(f"{game_directory}\\versions\\{version_name}\\{version_name}.json"))
    ntemp = f"{java} -Dfile.encoding=GB18030 -Dminecraft.client.jar={game_directory}\\versions\\{version_name}\\{version_name}.jar " \
            f"-XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -Djava.library.path={game_directory}\\versions\\{version_name}\\natives-windows-x86_64 " \
            f"-XX:G1NewSizePercent=20 -XX:-DontCompileHugeMethods " \
            f"-XX:G1ReservePercent=20 -XX:G1HeapRegionSize=16m -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow " \
            f"-Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.rmi.server.useCodebaseOnly=true " \
            f"-Dcom.sun.jndi.rmi.object.trustURLCodebase=false -Dcom.sun.jndi.cosnaming.object.trustURLCodebase=false " \
            f"-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump " \
            f"-Dlog4j2.formatMsgNoLookups=true -Dlog4j.configurationFile={game_directory}\\versions\\{version_name}\\log4j2.xml -cp"

    temp = f"{java} -Dfile.encoding=GB18030 -Dminecraft.client.jar={game_directory}\\versions\\{version_name}\\{version_name}.jar -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC " \
           f"-XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=16m -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -XX:-DontCompileHugeMethods " \
           f"-Xmn128m -Xmx3968m -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.rmi.server.useCodebaseOnly=true -Dcom.sun.jndi.rmi.object.trustURLCodebase=false -Dcom.sun.jndi.cosnaming.object.trustURLCodebase=false -Dlog4j2.formatMsgNoLookups=true -Dlog4j.configurationFile={game_directory}\\versions\\{version_name}\\log4j2.xml " \
           f"-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path={game_directory}\\versions\\{version_name}\\natives-windows-x86_64 -Dminecraft.launcher.brand=FMCL -Dminecraft.launcher.version=0.2 -cp"
    for i in ver_json['libraries']:
        if "name" in i:
            if ("downloads" not in i) or ("classifiers" not in i["downloads"]):
                name = i["name"].split(":")  # <package>:<name>:<version>
                name[0] = name[0].replace(".", "/")
                if not os.path.realpath(game_directory + "/libraries/" + i["name"]) in cps:
                    if ("rules" not in i) or ("os" not in i["rules"][0]):
                        cps.append(os.path.realpath(
                            f"{game_directory}\\libraries\\{name[0]}\\{name[1]}\\{name[2]}\\{name[1]}-{name[2]}.jar"))  # <package>/<name>/<version>/<name>-<version>.jar
    assets_root = os.path.abspath(game_directory + "\\assets")
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

    cp = ""
    for i in cps:
        cp += i + ';'

    temp1 = ""
    temp2 = ""

    print(ver_json.keys())
    if "minecraftArguments" in ver_json:
        temp1 = eval("f'" + getoptions(ver_json["minecraftArguments"]) + "'")
        print(temp1)

    if "arguments" in ver_json and "game" in ver_json["arguments"]:
        temp2 = eval("f'" + gethighoptions(ver_json["arguments"]["game"]) + "'")
        print(ver_json["arguments"]["game"])

    return f'{temp} {cp}{os.path.realpath(f"{game_directory}/versions/{version_name}/{version_name}.jar")} {ver_json["mainClass"]} {temp1} {temp2}'