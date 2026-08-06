def recommend_career(skills):

    if "Machine Learning" in skills or "Python" in skills:
        return "🤖 AI / Machine Learning Engineer"

    elif "SQL" in skills and "Python" in skills:
        return "📊 Data Analyst"

    elif "Java" in skills:
        return "☕ Java Developer"

    elif "HTML" in skills and "CSS" in skills:
        return "🌐 Front-End Developer"

    elif "Python" in skills:
        return "🐍 Python Developer"

    else:
        return "💻 Software Developer"