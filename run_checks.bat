@echo off
REM Runs the same checks as the CI pipeline: tests, coverage, Ruff.
call .venv\Scripts\activate.bat
echo === Tests with coverage ===
coverage run -m pytest -v
if errorlevel 1 exit /b 1
coverage report
coverage html
echo === Ruff lint ===
ruff check .
if errorlevel 1 exit /b 1
echo === Ruff format check ===
ruff format --check .
if errorlevel 1 exit /b 1
echo.
echo ALL CHECKS PASSED. Coverage report: htmlcov\index.html
