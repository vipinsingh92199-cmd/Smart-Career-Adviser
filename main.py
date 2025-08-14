from utils.input_handler import get_user_role, get_user_skills
from services.gap_analyzer import analyze_gaps
from services.genai_advisor import get_genai_advice

if __name__ == "__main__":
    role = get_user_role()
    user_skills = get_user_skills()

    matched, missing, courses = analyze_gaps(role, user_skills)

    print("\n=== Career Analysis ===")
    print(f"Matched Skills: {matched}")
    print(f"Missing Skills: {missing}")

    if missing:
        print("\nSuggested Courses:")
        for c in courses:
            print(f"- {c}")

    print("\n=== AI Career Advice ===")
    advice = get_genai_advice(role, matched, missing)
    for a in advice:
        print(f"- {a}")
