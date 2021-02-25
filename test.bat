@echo off

git log --pretty=format:\"%H\" -n 2 > .\\test.log
For /F "UseBackQ Delims==" %%A In (".\\test.log") Do Set "lastline=%%A"
Echo %lastline%