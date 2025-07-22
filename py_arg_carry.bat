@echo off
echo Python Args Carrier
echo.
echo Setting Python Path...

REM Força o diretório atual para onde o .bat está
cd /d "%~dp0"

REM Caminho para a venv
set VENV_PATH=%~dp0venv\Scripts\activate.bat

echo Activating Virtual Venv...
IF EXIST "%VENV_PATH%" (
    call "%VENV_PATH%"
) ELSE (
    echo ERROR: Virtual venv not in "%VENV_PATH%"
    exit /b
)
echo.

REM Agora o Python será o da venv
set PYTHON_EXE=python
set OUTPUT_DIR=%~dp0Dashboard\
set PYTHON_SCRIPT=%~dp0Python\generate_dashboard.py

echo/Today: %date%

set DAY=%date:~0,2%
set MONTH=%date:~3,2%
set YEAR=%date:~6,4%
echo.

REM Removes 0 if date is a single number
IF "%DAY:~0,1%"=="0" set "DAY=%DAY:~1%"
IF "%MONTH:~0,1%"=="0" set "MONTH=%MONTH:~1%"

echo --- Loading Arguments ---
set EXCEL_PROBLEM=Input\invoice_problem_%DAY%_%MONTH%_%YEAR%.xlsx
set EXCEL_PURCHASE=Input\purchase_plan_%DAY%_%MONTH%_%YEAR%.xlsx
echo.
echo.
echo.

echo Running Python script for Dashboard Generation...
echo Python Executable: %PYTHON_EXE%
echo Python Script: %PYTHON_SCRIPT%
echo Output Directory: %OUTPUT_DIR%
echo Excel File 1: %EXCEL_PROBLEM%
echo Excel File 2: %EXCEL_PURCHASE%
echo.

%PYTHON_EXE% %PYTHON_SCRIPT% --problema_path %EXCEL_PROBLEM% --invoice_path %EXCEL_PURCHASE% --output_dir %OUTPUT_DIR%

pause