def get_user_role():
    return input("Enter target role (e.g., data scientist): ").strip().lower()

def get_user_skills():
    skills_input = input("Enter your skills (comma-separated): ").lower()
    return [s.strip() for s in skills_input.split(",") if s.strip()]
