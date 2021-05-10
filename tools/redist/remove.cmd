rem @ECHO OFF

for /f "delims=|" %%f in ('dir /b /s "%~dp0*.dll"') do call :remove_file %%~nxf
goto :end

:remove_file
del "%~dp0..\..\%1"
del /s "%~dp0..\avisynth_plugin\%1"
del /s "%~dp0..\avs\%1"
del /s "%~dp0..\ffmpeg\%1"
del /s "%~dp0..\x264\%1"
del /s "%~dp0..\x265\%1"
del /s "%~dp0..\xvid\%1"
exit /b

:end