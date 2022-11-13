import core.mkdir
import view.core
import core.config
import os

if __name__ == "__main__":
    print("Using FMCL GUI 1.0 by Sharll.")
    if not os.path.exists("config.json"):
        core.config.write()
    core.mkdir.make_mc_dir(core.config.read()[".mc"])
    view.core.main()
