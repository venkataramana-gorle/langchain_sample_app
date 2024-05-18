@echo off
setlocal enabledelayedexpansion

set app_location=%cd%

REM Read properties file
for /f "tokens=1,* delims== " %%i in (env.properties) do (
    set "key=%%i"
    set "value=%%j"
    set "!key!=!value!"
)

docker stop langchain_sample_app > nul 2> nul
docker rm langchain_sample_app > nul 2> nul

docker build -t langchain_sample_app .
docker run -d --name langchain_sample_app -p !port!:5555 -v %app_location%:/app langchain_sample_app