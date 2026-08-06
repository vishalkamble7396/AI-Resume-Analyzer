import streamlit as st
from modules.auth import register, login
from modules.resume_parser import extract_text
from modules.skill_extractor import extract_skills
from modules.scorer import calculate_score
from modules.recommendation import missing_skills
from modules.career import recommend_career
import matplotlib.pyplot as plt
from modules.ats import ats_suggestions
from modules.pdf_report import create_pdf


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Sidebar
st.sidebar.title("📋 Menu")
menu = st.sidebar.radio(
    "Select Option",
    [
        "🏠 Home",
        "🔐 Login",
        "📝 Sign Up",
        "📤 Upload Resume",
        "📊 Dashboard",
        "ℹ About"
    ]
)

# Home Page
if menu == "🏠 Home":

    st.title("🤖 AI Resume Analyzer")

    st.subheader("Analyze Your Resume Using Artificial Intelligence")

    st.write(
        """
        Welcome to the AI Resume Analyzer Project.

        This application helps students and job seekers:
        - Analyze Resume
        - Extract Skills
        - Calculate Resume Score
        - Suggest Missing Skills
        - Recommend Job Roles
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📄 Upload Resume")

    with col2:
        st.success("🤖 AI Analysis")

    with col3:
        st.warning("💼 Career Recommendation")

# Login
elif menu == "🔐 Login":
    st.title("🔐 Login")

    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        user = login(email, password)

        if user:
            st.success(f"Welcome {user[1]}")
        else:
            st.error("Invalid Email or Password")

# Signup
elif menu == "📝 Sign Up":

    st.title("📝 Sign Up")

    full_name = st.text_input("Full Name", key="signup_name")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")

    if st.button("Create Account"):
        if register(full_name, email, password):
            st.success("Account Created Successfully!")
        else:
            st.error("Email Already Exists!")


# Upload Resume
elif menu == "📤 Upload Resume":

    st.title("📤 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Your Resume",
        type=["pdf"]
    )

    if uploaded_file is not None:
        st.success("✅ Resume Uploaded Successfully!")

        st.write("📄 File Name:", uploaded_file.name)
        st.write("📦 File Size:", round(uploaded_file.size / 1024, 2), "KB")
        resume_text = extract_text(uploaded_file)

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )
        skills = extract_skills(resume_text)

        st.subheader("🧠 Skills Found")

        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.warning("No skills found.")

        score = calculate_score(skills)

        st.subheader("📊 Resume Score")

        st.progress(score / 100)

        st.success(f"Your Resume Score is {score}/100")

        recommended = missing_skills(skills)

        st.subheader("📌 Recommended Skills")

        for skill in recommended[:8]:
            st.info(skill)

        career = recommend_career(skills)

        st.subheader("💼 Career Recommendation")

        st.success(career)

        st.session_state["skills"] = skills
        st.session_state["score"] = score
        st.session_state["missing"] = recommended
        st.session_state["career"] = career

        # Skills Extraction
        skills = extract_skills(resume_text)

        st.subheader("🧠 Skills Found")

        if skills:
                for skill in skills:
                    st.success(skill)
        else:
            st.warning("No skills found.")

        score = calculate_score(skills)

        st.subheader("📊 Resume Score")

        st.progress(score / 100)

        st.success(f"Your Resume Score is {score}/100")

        recommended = missing_skills(skills)

        st.subheader("📌 Recommended Skills")

        for skill in recommended[:8]:
            st.info(skill)

        career = recommend_career(skills)

        st.subheader("💼 Career Recommendation")

        st.success(career)


        suggestions = ats_suggestions()

        st.subheader("📋 ATS Suggestions")

        for suggestion in suggestions:
            st.info(suggestion)

        pdf_file = create_pdf(score, skills, career)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📥 Download Resume Report",
                data=file,
                file_name="Resume_Report.pdf",
                mime="application/pdf"
        )

# Dashboard
elif menu == "📊 Dashboard":

    st.title("📊 AI Resume Dashboard")

    if "score" not in st.session_state:
        st.warning("⚠ Please upload a resume first.")
        st.stop()

    score = st.session_state["score"]
    skills = st.session_state["skills"]
    missing = st.session_state["missing"]
    career = st.session_state["career"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📈 Resume Score", f"{score}/100")

    with col2:
        st.metric("🧠 Skills Found", len(skills))

    with col3:
        st.metric("❌ Missing Skills", len(missing))

    st.divider()

    st.subheader("💼 Career Recommendation")
    st.success(career)

    st.divider()

    st.subheader("🧠 Skills")

    for skill in skills:
        st.info(skill)

# About
elif menu == "ℹ About":
    st.title("About Project")
    st.write("AI Resume Analyzer using NLP and Python.")