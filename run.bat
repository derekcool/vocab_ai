@echo off

if [%1]==[] goto usage

python src/main.py %1
goto :eof
:usage
@echo Usage: run.bat ^<wordFile^>
exit /B 1
