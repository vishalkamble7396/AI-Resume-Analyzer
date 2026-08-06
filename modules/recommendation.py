def missing_skills(found_skills):

    all_skills = [
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

    missing = []

    for skill in all_skills:
        if skill not in found_skills:
            missing.append(skill)

    return missing