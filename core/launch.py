import json
import os


def getoptions(js: str):
    temp = ''
    for i in js.split("$"):
        temp += i
    return temp


def gethighoptions(js: list):
    temp = ""
    for i in js:
        if type(i) == str:
            temp += getoptions(i)+" "
        else:
            break
    return temp


def launch(game_directory: str = ".minecraft", version_name: str = None, java: str = "java",
           auth_player_name: str = "player"):
    if version_name is None:
        return 0
    if not (os.path.exists(game_directory) and os.path.exists(
            f"{game_directory}/versions/{version_name}/{version_name}.json")):
        return 1
    ver_json = json.load(open(f"{game_directory}\\versions\\{version_name}\\{version_name}.json"))
    temp = f"{java} -Dfile.encoding=utf-8 -Dminecraft.client.jar={game_directory}\\versions\\{version_name}\\{version_name}.jar -Djava.library.path={game_directory}\\versions\\{version_name}\\natives-windows-x86_64 -cp "
    for i in ver_json['libraries']:
        try:
            temp += (os.path.realpath(
                os.path.realpath(game_directory) + "/libraries/" + i['downloads']['artifact']['path']) + ";")
            print((os.path.realpath(
                os.path.realpath(game_directory) + "/libraries/" + i['downloads']['artifact']['path']) + ";"))
        except KeyError:
            try:
                print("Special: ", i['downloads']['classifiers'])
            except KeyError:
                name = i["name"].split(":")  # <package>:<name>:<version>
                tmp = ""
                for j in name[0]:
                    if j == ".":
                        tmp += "/"
                    else:
                        tmp += j
                name[0] = tmp
                temp += os.path.realpath(
                    f"{os.path.realpath(game_directory)}\\libraries\\{name[0]}\\{name[1]}\\{name[2]}\\{name[1]}-{name[2]}.jar;")  # <package>/<name>/<version>/<name>-<version>.jar
                print(os.path.realpath(
                    f"{os.path.realpath(game_directory)}\\libraries\\{name[0]}\\{name[1]}\\{name[2]}\\{name[1]}-{name[2]}.jar;")
                    # <package>/<name>/<version>/<name>-<version>.jar
                )

    assets_root = os.path.abspath(game_directory + "\\assets")
    assets_index_name = ver_json["assetIndex"]["id"]
    auth_uuid = "0"
    auth_access_token = "0"
    user_type = "Mojang"
    version_type = '"First Minecraft Launcher Demo"'
    user_properties = "{}"
    auth_session = "{}"

    try:
        return f'{temp}{os.path.realpath(f"{game_directory}/versions/{version_name}/{version_name}.jar")} {ver_json["mainClass"]} ' + eval(
            "f'" + getoptions(ver_json["minecraftArguments"] + "'"))
    except KeyError:

        return f'{temp}{os.path.realpath(f"{game_directory}/versions/{version_name}/{version_name}.jar")} {ver_json["mainClass"]} ' + eval('f"'+gethighoptions(ver_json["arguments"]["game"])+'"')

