@echo off
cls
del .\output\*.log
del .\output\*.x3d
del .\output\*.blend
del .\output\*.blend1

test.py
pause

