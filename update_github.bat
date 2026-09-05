@echo off

cd /d "D:\Learn\Flask"

echo ================================
echo   Updating The Magic Coder
echo ================================
echo.

echo [1/3] Adding changes...
git add .

echo.
echo [2/3] Creating commit...
git commit -m "Update The Magic Coder blog"

echo.
echo [3/3] Pushing to GitHub...
git push

echo.
echo ================================
echo   GitHub update completed!
echo ================================
pause