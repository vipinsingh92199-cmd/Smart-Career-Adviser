COURSES = {
    "python": ["Python for Everybody (Coursera)", "Automate the Boring Stuff"],
    "sql": ["Mode SQL Tutorial", "Khan Academy SQL"],
    "machine learning": ["Andrew Ng ML", "fast.ai Practical DL"],
    "react": ["React Docs Tutorial", "Fullstackopen"],
    "docker": ["Docker Mastery", "Kubernetes for Beginners"]
}

def course_suggestions(missing_skills):
    out = []
    for s in missing_skills:
        out.extend(COURSES.get(s, []))
    return out
