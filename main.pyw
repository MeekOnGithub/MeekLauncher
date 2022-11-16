import Core.System.CoreMakeFolderTask
import View.core
import Core.System.CoreConfigIO
import os

if __name__ == "__main__":
    if not os.path.exists("config.json"):
        Core.System.CoreConfigIO.write()
    Core.System.CoreMakeFolderTask.make_mc_dir(Core.System.CoreConfigIO.read()[".mc"])
    View.core.main()
