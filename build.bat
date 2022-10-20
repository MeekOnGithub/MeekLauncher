@echo off
echo First Minecraft Launcher by sharll. Packing on Pyinstaller.
pip install requests
pip install Pyinstaller
pyinstaller -F __main__.py
echo done.
pause
