def extract_skills(text):

    skills_db = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Science",
        "NLP",
        "TensorFlow",
        "PyTorch",
        "Pandas",
        "NumPy",
        "Flask",
        "Django",
        "Streamlit",
        "Git",
        "GitHub"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills