import os

import view.basic
import core.config
import core.mkdir

if __name__ == "__main__":
    make = core.mkdir.Files()
    make.make_mc_dir(".")
    if not os.path.exists("config.json"):
        core.config.write()
    print(core.config.read())
    view.basic.main()
