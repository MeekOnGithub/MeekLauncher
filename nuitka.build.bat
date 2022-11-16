@echo off
echo Welcome to FMCL nuitka build.
echo Nuitka has better performance, size.
echo Need to install something. Continue means you accept.
if EXIST "C:/Users/%Username%/Appdata/local/Programs/Python/Python310/Scripts/pip.exe" (
set pip="C:/Users/%Username%/Appdata/local/Programs/Python/Python310/Scripts/pip" 
) ELSE (
echo Can not find pip or python 3.10.
echo Warning: Python which are not 3.10 may cause some question.
set /p pip=Input your own pip path: 
)
pause
cls

echo Update pip.
%pip% install --upgrade pip
cls

echo Install Zstandard.
%pip% install zstandard
cls

echo Install Request
%pip% install requests
cls

echo Install Nuitka
%pip% install nuitka
cls

echo Starting build...
nuitka --standalone --onefile --include-data-files=view/icon.ico=view/icon.ico --plugin-enable=tk-inter --remove-output --disable-console main.pyw

pause
