from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import io
import os
import json
import re
import math
import httpx
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Resume Analyzer", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── SAMPLE JOB DATABASE ─────────────────────────────────────────────────────
JOB_DATABASE = []

# ─── SKILL DICTIONARY ─────────────────────────────────────────────────────────
SKILLS_DICT = [
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust", "kotlin", "swift",
    "ruby", "php", "scala", "r", "matlab", "bash", "shell", "sql", "nosql",
    "react", "angular", "vue", "next.js", "node.js", "express", "django", "flask", "fastapi",
    "spring", "hibernate", "laravel", "rails", "asp.net", "svelte",
    "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch",
    "scikit-learn", "keras", "huggingface", "transformers", "bert", "gpt", "spacy", "nltk",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly", "jupyter", "mlflow", "mlops",
    "docker", "kubernetes", "terraform", "ansible", "jenkins", "github actions", "ci/cd",
    "aws", "azure", "gcp", "lambda", "ec2", "s3", "cloudformation", "serverless",
    "postgresql", "mysql", "mongodb", "redis", "elasticsearch", "cassandra", "sqlite",
    "snowflake", "bigquery", "redshift", "spark", "hadoop", "kafka", "airflow", "dbt", "etl",
    "git", "linux", "agile", "scrum", "rest api", "graphql", "microservices", "devops",
    "html", "css", "tailwind", "bootstrap", "sass", "webpack", "vite",
    "android", "ios", "react native", "flutter", "firebase",
    "blockchain", "solidity", "ethereum", "web3.js", "smart contracts",
    "network security", "penetration testing", "siem", "vulnerability assessment",
    "data analysis", "statistics", "excel", "tableau", "power bi",
    "redux", "graphql", "websockets", "oauth", "jwt",
    "prometheus", "grafana", "datadog", "elk stack",
    "feature engineering", "a/b testing", "reinforcement learning",
]

# ─── ACTION VERBS ─────────────────────────────────────────────────────────────
ACTION_VERBS = [
    "developed", "implemented", "designed", "optimized", "built", "created", "led",
    "managed", "architected", "deployed", "automated", "improved", "reduced", "increased",
    "launched", "delivered", "collaborated", "mentored", "analyzed", "engineered",
    "integrated", "migrated", "refactored", "streamlined", "spearheaded", "established",
    "coordinated", "executed", "achieved", "scaled"
]

# ─── HELPERS ─────────────────────────────────────────────────────────────────

def normalize_text(text: str) -> str:
    return text.lower().strip()

def extract_skills_from_text(text: str) -> list:
    text_lower = normalize_text(text)
    found = []
    for skill in SKILLS_DICT:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found.append(skill)
    return list(set(found))

def extract_email(text: str) -> str:
    match = re.search(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}', text)
    return match.group(0) if match else ""

def extract_phone(text: str) -> str:
    match = re.search(r'(\+?\d[\d\s\-().]{7,}\d)', text)
    return match.group(0).strip() if match else ""

def extract_name(text: str) -> str:
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]
    for line in lines[:5]:
        if len(line.split()) <= 4 and not any(c in line for c in ['@', '/', 'http', '.']):
            if re.match(r'^[A-Za-z ]+$', line):
                return line
    return "Name Not Detected"

def detect_sections(text: str) -> dict:
    text_lower = text.lower()
    return {
        "education": bool(re.search(r'\b(education|university|college|degree|bachelor|master|phd|b\.?tech|m\.?tech|b\.?sc|m\.?sc)\b', text_lower)),
        "experience": bool(re.search(r'\b(experience|work history|employment|intern|position|role)\b', text_lower)),
        "projects": bool(re.search(r'\b(project|projects|built|developed|created)\b', text_lower)),
        "skills": bool(re.search(r'\b(skills|technologies|tools|competencies|tech stack)\b', text_lower)),
    }

def estimate_experience_level(text: str) -> str:
    text_lower = text.lower()
    if any(w in text_lower for w in ["senior", "lead", "principal", "staff", "director", "head of"]):
        return "Senior"
    if any(w in text_lower for w in ["mid", "intermediate", "3 years", "4 years", "5 years"]):
        return "Mid-Level"
    if any(w in text_lower for w in ["junior", "associate", "1 year", "2 years"]):
        return "Junior"
    if any(w in text_lower for w in ["intern", "fresher", "graduate", "entry", "student"]):
        return "Fresher"
    years = re.findall(r'(\d+)\+?\s*years?', text_lower)
    if years:
        max_years = max(int(y) for y in years)
        if max_years >= 6: return "Senior"
        if max_years >= 3: return "Mid-Level"
        if max_years >= 1: return "Junior"
    return "Fresher"

def predict_category(skills: list) -> str:
    category_map = {
        "Data Science": ["machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy", "nlp", "statistics", "mlops"],
        "Software Engineering": ["react", "node.js", "django", "flask", "javascript", "typescript", "rest api", "microservices"],
        "DevOps": ["docker", "kubernetes", "terraform", "ci/cd", "jenkins", "aws", "linux", "ansible", "prometheus"],
        "Data Engineering": ["spark", "hadoop", "kafka", "airflow", "etl", "snowflake", "dbt", "redshift", "bigquery"],
        "Mobile": ["android", "ios", "kotlin", "swift", "react native", "flutter", "firebase"],
        "Security": ["network security", "penetration testing", "siem", "vulnerability assessment"],
        "AI/ML": ["transformers", "bert", "gpt", "huggingface", "nlp", "computer vision", "reinforcement learning"],
        "Blockchain": ["solidity", "ethereum", "smart contracts", "web3.js", "blockchain"],
        "Cloud": ["aws", "azure", "gcp", "serverless", "lambda", "cloudformation"],
    }
    scores = {}
    skill_set = set(skills)
    for cat, cat_skills in category_map.items():
        scores[cat] = len(skill_set.intersection(set(cat_skills)))
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "Software Engineering"

def tfidf_cosine_similarity(resume_text: str, job_desc: str) -> float:
    def tokenize(text):
        words = re.findall(r'\b[a-z]{2,}\b', text.lower())
        stop = {"the","and","or","in","of","to","a","is","it","for","with","on","at","by","an","be","are","was","were","this","that","as","from","have","has","had","will","can","do","not","we","you","he","she","they","but","if","so"}
        return [w for w in words if w not in stop]
    
    def build_tf(tokens):
        tf = {}
        for t in tokens:
            tf[t] = tf.get(t, 0) + 1
        total = len(tokens) or 1
        return {k: v/total for k, v in tf.items()}
    
    resume_tokens = tokenize(resume_text)
    job_tokens = tokenize(job_desc)
    
    all_terms = set(resume_tokens + job_tokens)
    if not all_terms:
        return 0.0
    
    tf_r = build_tf(resume_tokens)
    tf_j = build_tf(job_tokens)
    
    def idf_weight(term):
        df = (term in tf_r) + (term in tf_j)
        return math.log(3 / (1 + df)) + 1
    
    vec_r = {t: tf_r.get(t, 0) * idf_weight(t) for t in all_terms}
    vec_j = {t: tf_j.get(t, 0) * idf_weight(t) for t in all_terms}
    
    dot = sum(vec_r[t] * vec_j[t] for t in all_terms)
    mag_r = math.sqrt(sum(v**2 for v in vec_r.values()))
    mag_j = math.sqrt(sum(v**2 for v in vec_j.values()))
    
    if mag_r == 0 or mag_j == 0:
        return 0.0
    return dot / (mag_r * mag_j)

def score_resume(text: str, skills: list, sections: dict) -> dict:
    text_lower = text.lower()
    scores = {}
    
    # 1. Skill Coverage (30)
    skill_score = min(30, len(skills) * 2)
    scores["skill_coverage"] = skill_score
    
    # 2. Experience Depth (20)
    exp_score = 0
    if re.search(r'\d+\s*\+?\s*years?', text_lower): exp_score += 8
    if any(w in text_lower for w in ["senior", "lead", "architect", "manager"]): exp_score += 7
    if sections["experience"]: exp_score += 5
    scores["experience_depth"] = min(20, exp_score)
    
    # 3. Projects (15)
    proj_score = 0
    if sections["projects"]: proj_score += 8
    proj_count = len(re.findall(r'\bproject\b', text_lower))
    proj_score += min(7, proj_count * 2)
    scores["project_relevance"] = min(15, proj_score)
    
    # 4. Impact Metrics (15)
    nums = re.findall(r'\d+%|\d+x|\$\d+|\d+\s*million|\d+\s*k\b', text_lower)
    scores["impact_metrics"] = min(15, len(nums) * 3)
    
    # 5. ATS Compatibility (10)
    ats = 0
    if sections["education"]: ats += 2
    if sections["skills"]: ats += 2
    if sections["experience"]: ats += 2
    if extract_email(text): ats += 2
    if extract_phone(text): ats += 2
    scores["ats_compatibility"] = ats
    
    # 6. Action Verbs (10)
    verb_count = sum(1 for v in ACTION_VERBS if v in text_lower)
    scores["action_verbs"] = min(10, verb_count * 2)
    
    total = sum(scores.values())
    scores["total"] = min(100, total)
    return scores

def get_improvement_tips(scores: dict, skills: list, sections: dict, text: str) -> list:
    tips = []
    if scores["impact_metrics"] < 10:
        tips.append("💡 Add quantifiable achievements (e.g., 'Improved performance by 40%', 'Reduced costs by $50K')")
    if scores["action_verbs"] < 6:
        tips.append("✍️ Start bullet points with strong action verbs like 'Developed', 'Architected', 'Led', 'Optimized'")
    if not sections["projects"]:
        tips.append("📁 Add a dedicated Projects section with 2-3 impactful technical projects")
    if scores["skill_coverage"] < 15:
        tips.append("🔧 Expand your Skills section — aim for 10+ relevant technical skills")
    if scores["ats_compatibility"] < 8:
        tips.append("📋 Ensure all key sections (Education, Experience, Skills) have clear headings for ATS systems")
    if len(skills) < 5:
        tips.append("🎯 Include more specific technologies and tools (frameworks, databases, cloud platforms)")
    if scores["experience_depth"] < 12:
        tips.append("📈 Elaborate on your experience with role titles, company names, and specific responsibilities")
    return tips[:5]

def keyword_density(text: str) -> dict:
    words = re.findall(r'\b[a-z]{4,}\b', text.lower())
    stop = {"with","that","this","have","from","they","will","been","were","your","about","would","could","which","there","their","what","when","more","also","into","than","then","some","time","work","used","each","well","make","most","over","such","like","just","very","take","each","only","both","much","many","long","down","same","after","back","other","these","those","here","should","through","before","being","using","including","during"}
    filtered = [w for w in words if w not in stop]
    freq = {}
    for w in filtered:
        freq[w] = freq.get(w, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:20])

# ─── API ENDPOINTS ─────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return FileResponse("ResumeAI-Standalone.html")

@app.get("/jobs")
def get_jobs():
    return {"jobs": JOB_DATABASE}

class TextAnalysisRequest(BaseModel):
    resume_text: str

@app.post("/analyze")
async def analyze_resume(request: TextAnalysisRequest):
    text = request.resume_text
    
    if len(text.strip()) < 50:
        raise HTTPException(status_code=400, detail="Resume text too short")
    
    # Extract info
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills_from_text(text)
    sections = detect_sections(text)
    exp_level = estimate_experience_level(text)
    category = predict_category(skills)
    scores = score_resume(text, skills, sections)
    tips = get_improvement_tips(scores, skills, sections, text)
    keyword_freq = keyword_density(text)
    
    # Job matching via TF-IDF cosine similarity
    job_matches = []
    for job in JOB_DATABASE:
        similarity = tfidf_cosine_similarity(text, job["description"])
        match_pct = round(similarity * 100 * 1.8, 1)
        match_pct = min(98.0, max(5.0, match_pct))
        
        missing = [s for s in job["skills"] if s not in skills][:5]
        
        job_matches.append({
            "id": job["id"],
            "title": job["title"],
            "category": job["category"],
            "match_percentage": match_pct,
            "missing_skills": missing,
        })
    
    job_matches.sort(key=lambda x: x["match_percentage"], reverse=True)
    top_jobs = job_matches[:5]
    
    return {
        "candidate": {
            "name": name,
            "email": email,
            "phone": phone,
            "experience_level": exp_level,
            "predicted_category": category,
        },
        "skills": skills,
        "skill_count": len(skills),
        "sections_detected": sections,
        "scores": scores,
        "top_jobs": top_jobs,
        "improvement_tips": tips,
        "keyword_density": keyword_freq,
    }

class ChatRequest(BaseModel):
    messages: List[Dict[str, Any]]
    system: Optional[str] = None
    max_tokens: int = 1000

@app.post("/chat")
async def chat_with_axiom(request: ChatRequest, x_api_key: Optional[str] = Header(None)):
    api_key = x_api_key or os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(status_code=401, detail="Missing API Key. Please provide an x-api-key header or set GROQ_API_KEY in the environment.")
    
    groq_url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "content-type": "application/json"
    }
    
    formatted_messages = []
    if request.system:
        formatted_messages.append({"role": "system", "content": request.system})
        
    for msg in request.messages:
        formatted_messages.append({"role": msg["role"], "content": msg["content"]})
    
    payload = {
        "max_tokens": request.max_tokens,
        "messages": formatted_messages
    }

    models_to_try = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "gemma2-9b-it"
    ]

    async with httpx.AsyncClient() as client:
        for model in models_to_try:
            payload["model"] = model
            try:
                response = await client.post(groq_url, headers=headers, json=payload, timeout=30.0)
                response.raise_for_status()
                
                data = response.json()
                return {
                    "content": [{"text": data["choices"][0]["message"]["content"]}]
                }
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429 and model != models_to_try[-1]:
                    continue
                raise HTTPException(status_code=e.response.status_code, detail=f"Groq API Error: {e.response.text}")
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=f"Failed to connect to Groq API: {str(e)}")

@app.get("/skills")
def get_all_skills():
    return {"skills": SKILLS_DICT}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
