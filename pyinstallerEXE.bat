@echo off
cd /d "%~dp0"

py -3.13 -m PyInstaller ^
SteamIconFixer.py ^
--noconsole ^
--name SteamIconFixer ^
--icon=SteamIconFixer.ico ^
--version-file version.txt ^
--noupx ^
--clean

pause