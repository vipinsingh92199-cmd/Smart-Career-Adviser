from data.role_skills import ROLE_SKILLS
from services.course_suggester import course_suggestions

def analyze_gaps(role, user_skills):
    req_skills = ROLE_SKILLS.get(role, [])
    matched = [s for s in req_skills if s in user_skills]
    missing = [s for s in req_skills if s not in user_skills]
    courses = course_suggestions(missing)
    return matched, missing, courses
