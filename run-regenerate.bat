@echo off
cd /d "c:\Users\OM\Documents\Matrics Mania"
powershell -NoProfile -ExecutionPolicy Bypass -Command "& '.\regenerate-pages.ps1'"
pause
