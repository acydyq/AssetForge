@echo off
cd /d C:\Users\Shadow\Documents\.PROJECTS\AssetForge
echo Staging changes...
git add .
echo Enter commit message:
set /p commit_message=
git commit -m "%commit_message%"

REM Ensure branch is set to "main"
git branch -M main
git push -u origin main

echo Changes pushed successfully.
pause
