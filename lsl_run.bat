@echo on

set "ORIGINAL_PATH=%CD%"

set "PIPENV=C:\Users\neuro\AppData\Local\Programs\Python\Python311\Scripts\pipenv.exe"
set "RUNPATH=C:\Users\neuro\nl-tools\"
set "EEGOPATH=C:\Users\neuro\Desktop\standalone-eego-edi1-lsl-outlet-v0.0.3\"
set "EEGO=C:\Users\neuro\Desktop\standalone-eego-edi1-lsl-outlet-v0.0.3\standalone_eego_edi1_lsl_outlet.exe"


cd %EEGOPATH%
start "LSL EEG" %EEGOPATH%start.bat"

cd %RUNPATH%
start "LSL Relay" %PIPENV% run lsl-relay --no-output

REM start "LSL Simulation" %PIPENV% run lsl-simulate -n 1 -s 2 --max-time 10 --debug

cd /d "%ORIGINAL_PATH%"


