@echo on

set "ORIGINAL_PATH=%CD%"

set "PIPENV=C:\Users\neuro\AppData\Local\Programs\Python\Python311\Scripts\pipenv.exe"
set "RUNPATH=C:\Users\neuro\nl-tools\"

cd %RUNPATH%

start "LSL remote control" %PIPENV% run lsl-ant-control --debug

cd /d "%ORIGINAL_PATH%"
