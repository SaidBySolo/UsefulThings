@echo off

set /p mode=1: Apply mod | 2: Unapply

cd %ProgramFiles(x86)%\Steam\steamapps\common\TEKKEN 7\TekkenGame\Content\Paks\~mods
if %mode%==1 (
    if not exist %cd%\Temporary (
        mkdir Temporary
    )
    move %cd%\FahkumGalaxyHead_P.pak %cd%Temporary
    echo Unapply complete.
    pause
)
if %mode%==2 (
    if exist %cd%\Temporary\FahkumGalaxyHead_P.pak (
        move %cd%\Temporary\FahkumGalaxyHead_P.pak %cd%
        echo Apply complete.
        pause
    ) else (
        echo error
    )
)