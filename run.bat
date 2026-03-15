@echo off
echo Starting AI Resume Analyzer Backend on port 8001...
start cmd /k "python backend_main.py"

echo Starting Frontend Server on port 8000...
start cmd /k "python -m http.server 8000"

echo Successfully started both servers in separate windows!
echo - Frontend UI: http://localhost:8000/ResumeAI-Standalone.html
echo - Backend API: http://localhost:8001
