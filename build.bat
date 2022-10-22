@echo off
color 8e
echo Welcome to FMCL build batchfile by Sharll. Pack by pyinstaller.
echo Pack must install pyinstaller and requests. Main.spec and all the things in ~/dist and ~/build will be deleted! 
set /p continue=Would you like to install?(y/n):
if not %continue%==y (
echo Because you decide not to install, the program must be quit.
pause
exit
)
if EXIST build rd /s /q build
if EXIST main.exe del main.exe
if EXIST main.spec del main.spec
set pip="C:/Users/%Username%/Appdata/local/Programs/Python/Python310/Scripts/pip" 
%pip% install pyinstaller
%pip% install requests
pyinstaller -F -w -i icon.ico --clean --add-data="icon.ico;." --distpath . main.py
if EXIST build rd /s /q build
if EXIST main.spec del main.spec
echo done.
pause
