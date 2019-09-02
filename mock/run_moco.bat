@echo off
set /p filename=input file name:
java -jar moco-runner-0.11.1-standalone.jar http -p 12306 -c %filename%
pause