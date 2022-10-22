@echo off
color 8e
echo Welcome to FMCL build batchfile by Sharll. Pack by pyinstaller.
set /p continue=Build must install pyinstaller and requests. Would you like to install?(y/n)
if not %continue%==y (
echo Because you decide not to install, the program must be quit.
pause
exit
)
set pip="C:/Users/%Username%/Appdata/local/Programs/Python/Python310/Scripts/pip" 
%pip% install pyinstaller
%pip% install requests
pyinstaller -F -w basic.py
echo done.
pause
