@echo off
rem -------------------------------------------------------------------
rem PATTERN2_PY.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

:begin
    set BATNAME=%~nx0
    echo —Ú‡Ú !BATNAME! ...

    set LIB_BAT=D:\PROJECTS_LYR\CHECK_LIST\SCRIPT\BAT\PROJECTS_BAT\TOOLS_SRC_BAT\SRC\LIB
    set PY_ENVDIR=D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\VENV

    set PY_ENVNAME=%PY_ENVNAME%
    if not defined PY_ENVNAME (
        set PY_ENVNAME=P313
    )
    if not exist !PY_ENVDIR!\!PY_ENVNAME! (
        echo INFO: Dir !PY_ENVDIR!\!PY_ENVNAME! not exist ...
        exit /b 1
    )

    set A1=%1
    if not defined A1 (
        echo INFO: A1 empty ...
        exit /b 1
    )
    set A2=%2
    if not defined A2 (
        echo INFO: A2 empty ...
        exit /b 1
    )
    set A3=%3
    if not defined A3 (
        echo INFO: A3 empty ...
        exit /b 1
    )
    
    call :PY_ENV_START || exit /b 1

    python %~dp0PATTERN2_PY.py "!A1!" "!A2!" "!A3!"

    call :PY_ENV_STOP || exit /b 1

    exit /b 0
:end
rem =================================================

rem =================================================
rem ‘”Õ ÷»» LIB
rem =================================================

rem =================================================
rem LYRPY.bat
rem =================================================
:LYRPY
%LIB_BAT%\LYRPY.bat %*
exit /b 0
:PY_ENV_START
%LIB_BAT%\LYRPY.bat %*
exit /b 0
:PY_ENV_STOP
%LIB_BAT%\LYRPY.bat %*
exit /b 0
