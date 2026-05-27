@echo off
rem Windows wrapper script for text replacement
rem Usage: replace_win.bat <target_file>

set "SCRIPT_DIR=%~dp0"

if "%1"=="" (
    echo Usage: %0 ^<target_file^>
    echo   ^<target_file^>  - Path to the text file to modify
    exit /b 1
)

python "%SCRIPT_DIR%replace.py" "%1"
