import os

BASE_URL = "https://jobs.dou.ua/vacancies/"
DATE_FORMAT = "%Y-%m-%d"

EXPERIENCE_LEVEL = {
    "all": "",
    "junior": "0-1",
    "middle": "1-3",
    "senior": "3-5",
    "senior+": "5plus"
}

CATEGORY = "?category=Python"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw") + "/"
CHARTS_DIR = os.path.join(BASE_DIR, "data", "charts") + "/"

NON_TECH_WORDS = {
    "Experience", "Strong", "Nice", "Senior", "Engineer", "Developer",
    "Build", "Design", "Knowledge", "English", "Preply", "Software",
    "Engineering", "Collaborate", "Development", "Familiarity", "Proven",
    "Implement", "Solid", "Tech", "Code", "Data", "Cloud", "Python", "API", "APIs",
    "REST", "SaaS", "LLM", "LLMs", "Develop", "Claude", "Backend", "Ability", "Google",
    "Experience", "Strong", "Nice", "Senior", "Engineer", "Developer",
    "Build", "Design", "Knowledge", "English", "Software", "Engineering",
    "Collaborate", "Development", "Familiarity", "Proven", "Implement",
    "Solid", "Tech", "Code", "Data", "Cloud", "Develop", "API", "APIs",
    "Junior", "Middle", "Lead", "Team", "Work", "Working", "Skills",
    "Join", "Looking", "Project", "System", "Service", "Platform",
    "Based", "Using", "Including", "Backend", "Production", "Business",
    "Client", "Management", "Product", "Stack", "Level", "Role",
    "Support", "Tools", "Security", "Solutions", "Architecture",
    "Testing", "Quality", "Performance", "Integration", "Ability", "Technical",
    "Professional", "Participate", "Integrate", "Contribute", "Actions", "Please",
    "Basic", "Understanding", "Competitive", "Growth", "Remote", "Full", "Europe",
    "Kyiv", "Ukraine", "Architect", "Manager", "Maintain", "Computer", "Science", "Automation",
    "Handle", "Operate", "Supportive", "Diagnose", "Debug", "Clear", "Intermediate", "Own", "Deep"
}
