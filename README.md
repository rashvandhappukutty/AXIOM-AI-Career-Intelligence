⚡ ResumeAI -- AI Resume Analyzer & Job Recommendation System
> **An AI-powered Resume Intelligence Platform that analyzes resumes,
> scores ATS compatibility, detects skill gaps, and recommends the most
> suitable jobs using NLP and Machine Learning.**
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![ML](https://img.shields.io/badge/Machine-Learning-orange)
![NLP](https://img.shields.io/badge/NLP-spaCy-green)
![Copyright](https://img.shields.io/badge/Copyright-All%20Rights%20Reserved-red)
---
📑 Table of Contents
Overview
Features
Architecture
Tech Stack
Project Structure
Installation
Environment Variables
Usage
API Endpoints
Machine Learning Pipeline
Algorithms Used
Resume Scoring
Sample Output
Future Scope
Author
Copyright
---
📖 Overview
ResumeAI is a full-stack AI-powered Resume Intelligence Platform built
with React, FastAPI, NLP, and Machine Learning. It parses resumes,
extracts skills, predicts job categories, scores ATS compatibility,
detects missing skills, and recommends the best-matching jobs using
TF-IDF and Cosine Similarity.
✨ Features
PDF & DOCX Resume Upload
Resume Parsing
Skill Extraction using spaCy
Named Entity Recognition
ATS Score
Resume Score (100 points)
Job Recommendation Engine
Skill Gap Detection
Claude AI Suggestions
Experience Level Prediction
Dashboard with Charts & Analytics
🏗 Architecture
``` text
React Frontend
      │
 REST API
      │
FastAPI Backend
 ├── Resume Parser
 ├── NLP Engine
 ├── TF-IDF Matcher
 ├── Resume Scoring
 ├── Category Prediction
 └── Claude AI Integration
```
🛠 Tech Stack
Layer      Technology
---
Frontend   React, Vite
Backend    FastAPI, Python
NLP        spaCy, Regex, PhraseMatcher
ML         TF-IDF, Cosine Similarity
AI         Claude Sonnet
Database   SQLite / PostgreSQL
📂 Project Structure
``` text
resume-ai/
├── backend/
├── frontend/
├── README.md
└── LICENSE
```
🚀 Installation
Frontend
``` bash
npm install
npm run dev
```
Backend
``` bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
🔐 Environment Variables
``` env
ANTHROPIC_API_KEY=your_api_key
DATABASE_URL=sqlite:///resume.db
```
▶️ Usage
Upload Resume
Resume is parsed
Skills extracted
Resume scored
Jobs matched
AI suggestions displayed
🌐 API Endpoints
Method   Endpoint   Description
---
POST     /upload    Upload resume
POST     /analyze   Analyze resume
GET      /jobs      List jobs
GET      /health    Health check
🤖 Machine Learning Pipeline
Resume → Text Extraction → Cleaning → Skill Extraction → TF-IDF → Cosine
Similarity → Ranking → Resume Score → AI Suggestions
🧠 Algorithms Used
TF-IDF Vectorization
Cosine Similarity
Phrase Matching
Regex
Named Entity Recognition
Weighted Scoring
📊 Resume Scoring
Criteria           Score
---
Skills                30
Experience            20
Projects              15
Impact Metrics        15
ATS                   10
Action Verbs          10
Total: 100
📈 Sample Output
Resume Score: 89/100
ATS Score: 92%
Category: AI Engineer
Top Match: Machine Learning Engineer (95%)
🔮 Future Scope
Resume Builder
Cover Letter Generator
LinkedIn Analysis
GitHub Analysis
AI Interview Coach
Recruiter Dashboard
RAG Resume Review
👨‍💻 Author
Rashvandh A
AI & Machine Learning Engineer | Full Stack Developer
---
📄 Copyright & License
© Copyright 2026 Rashvandh A. All Rights Reserved.
ResumeAI and all associated source code, documentation, machine learning
models, algorithms, UI/UX designs, datasets, graphics, and assets are
the exclusive intellectual property of Rashvandh A.
This repository is provided solely for educational demonstration and
portfolio purposes.
You may NOT:
Copy or reproduce this project.
Modify or create derivative works.
Redistribute the source code.
Publish under another name.
Sell or commercially use this project.
Claim ownership of this work.
Disclaimer
This software is provided AS IS without warranty of any kind.
© 2026 Rashvandh A. All Rights Reserved.
