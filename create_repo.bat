@echo off
cd /d C:\Users\Shadow\Documents\.PROJECTS\AssetForge
echo Initializing Git repository...
git init
echo Enter your GitHub repository name:
set /p repo_name=
echo Enter your GitHub username:
set /p username=
echo Creating remote repository on GitHub...
curl -u %username% https://api.github.com/user/repos -d "{\"name\":\"%repo_name%\"}"
git remote add origin https://github.com/%username%/%repo_name%.git
echo Repository created and linked successfully.
pause
