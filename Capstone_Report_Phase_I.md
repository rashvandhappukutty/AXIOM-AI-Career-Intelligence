
### CONTENTS

| Section No. | Section Title | Page No. |
| :--- | :--- | :--- |
| | Acknowledgment | 2 |
| | Contents | 3 |
| | Synopsis | 4 |
| 1. | **Introduction** | 5-8 |
| | 1.1 Organization Profile | |
| | 1.2 System Specification | |
| | 1.3 Hardware Configuration | |
| | 1.4 Software Specification | |
| 2. | **System Study** | 9-11 |
| | 2.1 Existing System | |
| | 2.2 Drawbacks | |
| | 2.3 Proposed System | |
| | 2.4 Features | |
| 3. | **System Design and Development** | 12-18 |
| | 3.1 File Design | |
| | 3.2 Input Design | |
| | 3.3 Output Design | |
| | 3.4 Database Design | |
| | 3.5 System Development | |
| | 3.6 Description of Modules | |
| 4. | **Software Testing and Implementation** | 19-22 |
| 5. | **Conclusion** | 23-24 |
| 6. | **Bibliography** | 25-26 |
| 7. | **Appendices** | 27-32 |
| | A. Data Flow Diagram | |
| | B. Table Structure | |
| | C. Sample Coding | |
| | D. Sample Input | |
| | E. Sample Output | |

---

### Synopsis

In the modern job market, HR professionals are inundated with hundreds of resumes for every job opening, making manual screening highly inefficient and prone to bias. This project introduces **AI Resume Analyzer**, an intelligent recruitment assistance system that leverages machine learning and natural language processing (NLP) to automate the evaluation of candidate profiles.

The system utilizes a custom **TF-IDF (Term Frequency-Inverse Document Frequency) Cosine Similarity** algorithm to match resumes against job descriptions with high precision. Key features include **automated skill extraction** using regular expressions and a comprehensive technical skill dictionary, **ATS (Applicant Tracking System) scoring** based on multiple criteria (skill coverage, experience depth, projects, and impact metrics), and a **Quantum Draft Chatbot** powered by advanced Large Language Models (LLMs) via the Groq API for real-time career guidance.

The architecture consists of a robust **FastAPI backend** for high-performance data processing and a premium, responsive **standalone HTML5/JS frontend** featuring a futuristic "Axiom" design aesthetic. By integrating data science with modern web technologies, AI Resume Analyzer provides a fast, reliable, and bias-free tool for early talent filtering, significantly enhancing the efficiency of the hiring process.

---

### 1. Introduction

With the rapid growth of the digital economy, the volume of job applications has increased exponentially. Traditional recruitment methods, where hiring managers manually scan each resume, are no longer sustainable. This project focuses on developing an AI-powered resume analysis system that intelligently pre-screens candidates, saving time and improving the quality of hire.

The **AI Resume Analyzer** project objective is to create a tool that not only parses resumes but also provides actionable insights, such as keyword density, improvement tips, and a matching score for specific job roles within its database.

#### Project Objectives
- **Automated Information Extraction**: Parse resumes to extract contact information, education, skills, and experience levels.
- **Role Classification**: Predict the candidate's professional category based on their skill set.
- **Match Analysis**: Calculate the similarity between a resume and various job descriptions using TF-IDF and Cosine Similarity.
- **ATS Optimization**: Provide a detailed scoring breakdown and suggestions to help candidates make their resumes more ATS-friendly.
- **Interactive AI Support**: Implement a chat interface for candidates to ask career-related questions and receive instant AI-driven responses.

#### Significance of the Project
By bridging the gap between raw resume data and recruitment requirements, this project empowers HR departments with a data-driven decision-making tool. It ensures that top talent is not overlooked due to manual fatigue and provides candidates with immediate feedback to improve their professional presentation.

---

### 2. System Study

#### 2.1 Existing System
The current recruitment process largely involves manual screening by HR recruiters or basic keyword-based ATS systems that often fail to understand context or semantic similarity.

#### 2.2 Drawbacks of the Existing System
- **Subjective Bias**: Manual screening is prone to human bias and inconsistent evaluation.
- **Inefficiency**: Sorting through large volumes of resumes takes excessive man-hours.
- **Lack of Feedback**: Candidates often receive no feedback on why their resume was rejected.
- **Semantic Gap**: Basic systems might miss qualified candidates if they don't use exact keyword matches.

#### 2.3 Proposed System
The proposed **AI Resume Analyzer** addresses these gaps by:
- **Intelligent Matching**: Using TF-IDF vectorization to understand the semantic importance of terms.
- **Multi-Criteria Scoring**: Evaluating resumes based on impact, action verbs, and section completeness, not just keywords.
- **Real-time Deployment**: Using a lightweight, high-speed FastAPI backend.
- **Premium User Experience**: Providing a "Quantum" UI that is both functional and visually stunning.

#### 2.4 Features
1. **Resume Parsing**: Extracts Name, Email, Phone, and Experience level automatically.
2. **Skill Ranking**: Identifies and categorizes technical skills from a deep dictionary.
3. **Job Match Dashboard**: Shows the top 5 job matches from the database with match percentages.
4. **Improvement Insights**: Generates tips based on scoring modules like "Impact Metrics" and "Action Verbs".
5. **Interactive Chat**: A Groq-API-powered AI assistant for career coaching.
6. **PDF Integration**: Frontend support for rendering and interacting with PDF files.

---

### 3. System Design and Development

#### 3.1 File Design
- `backend_main.py`: The core FastAPI server handling processing, logic, and AI integration.
- `index.html`: The main entry point for the "Quantum Draft" UI.
- `ResumeAI-Standalone.html`: A portable, all-in-one frontend version.
- `JOB_DATABASE`: In-memory JSON-structured database of job roles.

#### 3.2 Input Design
- **Format**: PDF (.pdf) or Plain Text (.txt) resumes.
- **Upload**: Drag-and-drop or file browser interface.
- **Parameters**: Text extracted from the resume file.

#### 3.3 Output Design
- **ATS Score**: 0-100 score with a detailed breakdown.
- **Job Recommendations**: List of matching titles and missing skills.
- **Career Tips**: Categorized suggestions for improvement.
- **Visual Charts**: Keyword density and skill distribution visualizations.

#### 3.4 Database Design (In-memory)
The system uses a structured `JOB_DATABASE` list containing:
- `id`, `title`, `category`, `description`, `skills`.

#### 3.5 System Development
- **Tech Stack**: Python, FastAPI, JavaScript, HTML5, CSS3 (Vanilla), Groq LLM API.
- **Methodology**: Agile development with iterative improvements to the parsing engine.

#### 3.6 Description of Modules
1. **Extraction Module**: Uses regex to identify emails, phones, and names.
2. **Scoring Engine**: Calculates points for Skill Coverage, Experience, Projects, Impact, and ATS Compatibility.
3. **Matching Module**: Implements TF-IDF vectorization and Cosine Similarity calculation.
4. **AI Communication Module**: Interfaces with Groq SDK for real-time chat functionality.

---

### 4. Software Testing and Implementation

#### 4.1 Testing Strategies
- **Unit Testing**: Testing individual regex patterns and scoring functions.
- **Integration Testing**: Verifying the data flow from resume upload to score calculation.
- **Functional Testing**: Ensuring the AI chat responds accurately to diverse prompts.
- **Performance Testing**: Measuring response times for TF-IDF calculations on larger files.

#### 4.2 Implementation Process
- **Environment Setup**: Python 3.10+, FastAPI installation, and API Key configuration.
- **Backend Deployment**: Running the server using Uvicorn.
- **Frontend Integration**: Connecting the JS fetch calls to the FastAPI endpoints.

---

### 5. Conclusion

The **AI Resume Analyzer** represents a significant step forward in automating the talent acquisition workflow. By combining traditional NLP techniques like TF-IDF with modern LLM-based assistants, the system provides a holistic evaluation of a candidate's profile.

---

### 6. Bibliography

1. Salton, G., & Buckley, C. (1988). **Term-weighting approaches in automatic text retrieval**. Information Processing & Management.
2. **FastAPI Documentation**. (2024). High-performance Python API framework.
3. **Groq API Documentation**. (2024). LPU Inference Engine for Large Language Models.
4. **PDF.js Documentation**. (2024). Mozilla's PDF reader for the web.

---

### 7. Appendices

#### B. Sample Coding: Main Analysis Endpoint
```python
@app.post("/analyze")
async def analyze_resume(request: TextAnalysisRequest):
    text = request.resume_text
    
    # Information Extraction
    skills = extract_skills_from_text(text)
    exp_level = estimate_experience_level(text)
    category = predict_category(skills)
    
    # Scoring and Job Matching
    scores = score_resume(text, skills, detect_sections(text))
    job_matches = []
    for job in JOB_DATABASE:
        similarity = tfidf_cosine_similarity(text, job["description"])
        job_matches.append({
            "title": job["title"],
            "match_percentage": round(similarity * 100 * 1.8, 1)
        })
    
    return {"candidate": {"experience": exp_level}, "scores": scores, "top_matches": job_matches}
```

#### C. Sample Coding: Scoring Algorithm
```python
def score_resume(text, skills, sections):
    scores = {}
    # 1. Skill Coverage (30)
    scores["skill_coverage"] = min(30, len(skills) * 2)
    # 2. Experience Depth (20)
    exp_score = 15 if any(w in text.lower() for w in ["senior", "lead"]) else 8
    scores["experience_depth"] = exp_score
    # 3. Impact Metrics (15)
    nums = re.findall(r'\d+%|\d+x|\$\d+', text)
    scores["impact_metrics"] = min(15, len(nums) * 3)
    # 4. ATS Compatibility (10)
    ats = 0
    if sections["education"]: ats += 5
    if sections["experience"]: ats += 5
    scores["ats_compatibility"] = ats
    
    scores["total"] = sum(scores.values())
    return scores
```

#### C. Sample Input (Resume Text)
"Experienced Software Engineer with a background in Python, React, and AWS. Developed a microservices architecture that reduced latency by 40%..."

#### D. Sample Output
"ATS Score: 85/100. Strong match for Senior Python Developer (92.5%). Tip: Add more quantifiable projects."
