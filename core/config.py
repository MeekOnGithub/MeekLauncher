import json
import os
from multiprocessing import cpu_count

config = os.path.abspath("config.json")


def read():
    return json.load(open(config, "r+"))


def write(playername: str = "player", dotmc: str = ".minecraft", java: str = "java", ram: str = "1024M",
          threads: int = cpu_count() * 8):
    con = {"playername": playername, ".mc": dotmc, "java": java, "ram": ram, "threads": threads}
    open(config, "w+").write(json.dumps(con))
