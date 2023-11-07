@echo on

set "ORIGINAL_PATH=%CD%"

set "PIPENV=C:\Users\neuro\AppData\Local\Programs\Python\Python311\Scripts\pipenv.exe"
set "RUNPATH=C:\Users\neuro\nl-tools\"
set "EEGOPATH=C:\Users\neuro\Desktop\standalone-eego-edi1-lsl-outlet-v0.0.3\"
set "EEGO=C:\Users\neuro\Desktop\standalone-eego-edi1-lsl-outlet-v0.0.3\standalone_eego_edi1_lsl_outlet.exe"



cd %RUNPATH%
REM %PIPENV% update

%PIPENV% --rm
%PIPENV% install

cd /d "%ORIGINAL_PATH%"


