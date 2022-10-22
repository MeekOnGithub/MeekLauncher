@echo off
echo First Minecraft Launcher by sharll. Packing on Pyinstaller.
pip install requests
pip install Pyinstaller
pyinstaller -F basic.py
echo done.
pause
