@echo off
cd /d C:\Users\Shadow\Documents\.PROJECTS\AssetForge
echo Building standalone executable...
pyinstaller --onefile --windowed src/main.py --name AssetForge
echo Build complete. Check the 'dist' folder for the executable.
pause
