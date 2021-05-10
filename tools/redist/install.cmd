rem @ECHO OFF

rem ********************************************************************************************
rem AVS expects the DLL files in the MeGUI root & encoder directories
rem AVS+ expects the DLL files in the filter directories
rem therefore copy all redist files into all of these directories if they are not installed yet
rem ********************************************************************************************

rem 2010_x86
REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products /s /f "Microsoft Visual C++ 2010  x86 Redistributable"
if errorlevel 1 (
  call :copy_files "%~dp02010_x86"
)

rem 2017_x86
REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Dependencies /s /f "Microsoft Visual C++ 2017 Redistributable (x86)"
if errorlevel 1 (
  call :copy_files "%~dp02017_x86"
)

goto :end

:copy_files
copy /y "%1\*.dll" "%~dp0..\.."
if exist "%~dp0..\avisynth_plugin" copy /y "%1\*.dll" "%~dp0..\avisynth_plugin"
if exist "%~dp0..\avs" copy /y "%1\*.dll" "%~dp0..\avs"
if exist "%~dp0..\ffmpeg" copy /y "%1\*.dll" "%~dp0..\ffmpeg"
if exist "%~dp0..\x264" copy /y "%1\*.dll" "%~dp0..\x264"
if exist "%~dp0..\x265" copy /y "%1\*.dll" "%~dp0..\x265"
if exist "%~dp0..\xvid" copy /y "%1\*.dll" "%~dp0..\xvid"
exit /b

:end