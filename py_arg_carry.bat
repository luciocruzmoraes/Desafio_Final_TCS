@echo off
echo Python Args Carrier
echo.
echo Setting Python Path...
echo.
set PYTHON_EXE="python"
set PYTHON SCRIPT="C:\Python\generate_dashborad.py"

echo/Hoje: %date%
set DAY=%date:~0,2%
set MONTH=%date:~3,2%
set YEAR=%date:~6,4%
echo.

echo --- Loading Arguments ---
set EXCEL_PROBLEM="C:\Input\invoice_problem_%DAY%_%MONTH%_%YEAR%.xlsx"
set EXCEL_PURCHASE="C:\Input\purchase_plan_%DAY%_%MONTH%_%YEAR%.xlsx"
echo.

echo .
echo .
echo .

echo.
echo Running Python script for Dashboard Generation...
echo Python Executable: %PYTHON_EXE%
echo Python Script: %PYTHON_SCRIPT%
echo Excel File 1: %EXCEL_PROBLEM%
echo Excel File 2: %EXCEL_PURCHASE%
echo.

pause