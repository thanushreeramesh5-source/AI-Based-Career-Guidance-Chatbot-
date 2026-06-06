import streamlit as st
import sqlite3
from datetime import datetime

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="AI Smart Career Guidance System",
    page_icon="🎯",
    layout="wide"
)

# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------
conn = sqlite3.connect("career_guidance.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    percentage REAL,
    interest TEXT,
    skill TEXT,
    goal TEXT,
    created_at TEXT
)
""")
conn.commit()


# -----------------------------------
# FUNCTIONS
# -----------------------------------
def save_user(name, email, password, percentage, interest, skill, goal):
    c.execute("""
        INSERT INTO users
        (name, email, password, percentage, interest, skill, goal, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        email,
        password,
        percentage,
        interest,
        skill,
        goal,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()


def career_recommendation(interest, marks):
    if interest == "Coding" and marks >= 75:
        return {
            "career": "Software Engineering / AI / Data Science",
            "certifications": "Python, SQL, Machine Learning, Cloud Computing",
            "internships": "Software Developer Intern, Data Analyst Intern",
            "companies": "Infosys, TCS, Wipro, Accenture, Google",
            "prep": "DSA, Aptitude, Coding Practice, Mock Interviews"
        }

    elif interest == "Electrical" and marks >= 70:
        return {
            "career": "Core EEE / Power Systems / PSU Jobs",
            "certifications": "MATLAB, AutoCAD, PLC, SCADA",
            "internships": "Power Plant Intern, Electrical Design Intern",
            "companies": "ABB, Siemens, BHEL, BEL",
            "prep": "GATE Preparation, PSU Exams, Core Subjects"
        }

    elif interest == "Biology":
        return {
            "career": "Medical / Pharmacy / Biotechnology",
            "certifications": "Clinical Research, Bioinformatics",
            "internships": "Hospital Internship, Pharma Company",
            "companies": "Apollo, Cipla, Biocon",
            "prep": "NEET / Research / Higher Studies"
        }

    elif interest == "Government Jobs":
        return {
            "career": "UPSC / SSC / Banking / Railways",
            "certifications": "Aptitude + Reasoning + Current Affairs",
            "internships": "Skill Development Programs",
            "companies": "Government Sector",
            "prep": "Mock Tests, Current Affairs, Competitive Exams"
        }

    else:
        return {
            "career": "MBA / Entrepreneurship / Startup",
            "certifications": "Finance, Leadership, Digital Marketing",
            "internships": "Startup Internships, Business Analyst Intern",
            "companies": "Corporate Management Roles / Startups",
            "prep": "Communication Skills, Leadership, Management"
        }


def personality_result(score):
    if score >= 3:
        return "You are highly leadership-oriented and confident."
    elif score == 2:
        return "You have balanced teamwork and analytical skills."
    else:
        return "You should focus on communication and confidence-building."


def resume_analysis(text, interest, goal):
    suggestions = []
    text = text.lower()

    # Common Resume Checks
    if "internship" not in text:
        suggestions.append("Add internship experience relevant to your domain")

    if "project" not in text:
        suggestions.append("Include major academic/project work with outcomes")

    if "skill" not in text:
        suggestions.append("Improve technical skills section with tools/software")

    if "linkedin" not in text:
        suggestions.append("Add LinkedIn profile for professional visibility")

    if "github" not in text and interest == "Coding":
        suggestions.append("Add GitHub profile with project repositories")

    if "certification" not in text:
        suggestions.append("Include certifications to strengthen your profile")

    if "achievement" not in text:
        suggestions.append("Add measurable achievements and accomplishments")

    if "objective" not in text:
        suggestions.append("Write a strong career objective section")

    # Domain-Based Suggestions
    if interest == "Coding":
        suggestions.append("Highlight Python, SQL, DSA, Projects, Internships")
        suggestions.append("Mention Hackathons, Coding Platforms, GitHub Links")

    elif interest == "Electrical":
        suggestions.append("Highlight MATLAB, AutoCAD, PLC, SCADA knowledge")
        suggestions.append("Add mini-projects related to Power Systems")

    elif interest == "Biology":
        suggestions.append("Highlight Lab Skills, Clinical Research")
        suggestions.append("Include Hospital/Pharma internship exposure")

    elif interest == "Government Jobs":
        suggestions.append("Highlight Aptitude, Communication, Leadership")
        suggestions.append("Mention Certifications for Competitive Exams")

    elif interest == "Business":
        suggestions.append("Highlight Leadership, Finance, Marketing Skills")
        suggestions.append("Add Startup Projects or Entrepreneurship Activities")

    # Goal-Based Suggestions
    if goal == "Higher Studies":
        suggestions.append("Add research papers, seminars, academic achievements")

    elif goal == "Job":
        suggestions.append("Focus more on internships and certifications")

    elif goal == "Government Exams":
        suggestions.append("Highlight discipline and aptitude strengths")

    elif goal == "Business":
        suggestions.append("Add business case studies and leadership work")

    if len(suggestions) == 0:
        suggestions.append("Your resume is strong. Only formatting improvements needed.")

    return suggestions


def generate_roadmap(interest, goal):
    roadmap = []

    if interest == "Coding":
        roadmap = [
            "Month 1: Learn Python, SQL, Data Structures Basics",
            "Month 2: Complete Certification in Python / Data Science",
            "Month 3: Build Mini Projects + GitHub Portfolio",
            "Month 4: Resume + LinkedIn + Internship Applications",
            "Month 5: Aptitude + Coding Interview + Mock Interviews",
            "Month 6: Placement Drives + Company Applications"
        ]

    elif interest == "Electrical":
        roadmap = [
            "Month 1: Strengthen Core Subjects",
            "Month 2: Learn MATLAB, AutoCAD, PLC Basics",
            "Month 3: Mini Project + Technical Certification",
            "Month 4: Resume + Core Company Applications",
            "Month 5: GATE / PSU Preparation",
            "Month 6: Mock Interviews + Placement Preparation"
        ]

    elif interest == "Biology":
        roadmap = [
            "Month 1: Clinical Basics + Domain Strengthening",
            "Month 2: Certification in Bioinformatics",
            "Month 3: Resume + Internship Search",
            "Month 4: Project Work + Research Preparation",
            "Month 5: Higher Studies / NEET Preparation",
            "Month 6: Final Applications + Interview Preparation"
        ]

    elif interest == "Government Jobs":
        roadmap = [
            "Month 1: Syllabus Understanding",
            "Month 2: Aptitude + Reasoning + Current Affairs",
            "Month 3: Mock Tests + Time Management",
            "Month 4: Revision + Previous Year Papers",
            "Month 5: Full-Length Test Series",
            "Month 6: Final Preparation + Exam Strategy"
        ]

    else:
        roadmap = [
            "Month 1: Leadership + Business Fundamentals",
            "Month 2: Finance + Digital Marketing Certification",
            "Month 3: Startup Case Studies + Mini Projects",
            "Month 4: Resume + LinkedIn + Internship Applications",
            "Month 5: Communication + Presentation Skills",
            "Month 6: Corporate Placement + Startup Opportunities"
        ]

    if goal == "Higher Studies":
        roadmap.append("Extra Focus: Research Papers + Entrance Exam Preparation")

    elif goal == "Government Exams":
        roadmap.append("Extra Focus: Daily Mock Tests + Current Affairs")

    elif goal == "Business":
        roadmap.append("Extra Focus: Startup Planning + Financial Management")

    return roadmap


# -----------------------------------
# UI HEADER
# -----------------------------------
st.title("🎯 AI-Based Smart Career Guidance System")
st.write("Final-Year Major Project - Advanced Version")
st.markdown("---")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Student Login/Register",
        "Career Guidance",
        "Personality Test",
        "Resume Suggestions",
        "6-Month Roadmap",
        "Admin Dashboard"
    ]
)


# -----------------------------------
# STUDENT LOGIN / REGISTER
# -----------------------------------
if menu == "Student Login/Register":
    st.subheader("Student Registration")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if name and email and password:
            save_user(name, email, password, 0, "", "", "")
            st.success("Registration Successful!")
            st.info("Now proceed to Career Guidance section.")
        else:
            st.warning("Please fill all fields.")


# -----------------------------------
# CAREER GUIDANCE
# -----------------------------------
elif menu == "Career Guidance":
    st.subheader("AI Career Recommendation Engine")

    name = st.text_input("Enter Your Name")
    marks = st.number_input("Percentage", min_value=0.0, max_value=100.0)

    interest = st.selectbox(
        "Main Interest",
        ["Coding", "Electrical", "Biology", "Government Jobs", "Business"]
    )

    skill = st.text_input("Current Skill")

    goal = st.selectbox(
        "Future Goal",
        ["Job", "Higher Studies", "Government Exams", "Business"]
    )

    if st.button("Get Full Recommendation"):
        result = career_recommendation(interest, marks)

        save_user(
            name,
            "demo@email.com",
            "demo",
            marks,
            interest,
            skill,
            goal
        )

        st.success(f"Recommended Career Path: {result['career']}")
        st.info(f"Certification Recommendations: {result['certifications']}")
        st.write(f"Internship Suggestions: {result['internships']}")
        st.write(f"Company / Role Matching: {result['companies']}")
        st.write(f"Placement Preparation Guidance: {result['prep']}")

        st.subheader("Soft Skill Recommendations")
        st.write("Communication, Leadership, Teamwork, Time Management")

        st.subheader("AI Chatbot Suggestion")
        st.write(
            f"Hello {name}, based on your interest in {interest}, "
            f"your best career path is {result['career']}. "
            f"Focus on certifications and internships for faster placement success."
        )


# -----------------------------------
# PERSONALITY TEST
# -----------------------------------
elif menu == "Personality Test":
    st.subheader("Personality Test")

    q1 = st.radio("Do you enjoy solving logical problems?", ["Yes", "No"])
    q2 = st.radio("Do you prefer teamwork?", ["Yes", "No"])
    q3 = st.radio("Are you comfortable speaking publicly?", ["Yes", "No"])
    q4 = st.radio("Do you like taking leadership responsibility?", ["Yes", "No"])

    if st.button("Analyze Personality"):
        score = [q1, q2, q3, q4].count("Yes")
        result = personality_result(score)
        st.success(result)


# -----------------------------------
# RESUME SUGGESTIONS
# -----------------------------------
elif menu == "Resume Suggestions":
    st.subheader("Advanced Resume Improvement Suggestions")

    resume_text = st.text_area("Paste Your Resume Summary")

    interest = st.selectbox(
        "Select Your Domain",
        ["Coding", "Electrical", "Biology", "Government Jobs", "Business"]
    )

    goal = st.selectbox(
        "Career Goal",
        ["Job", "Higher Studies", "Government Exams", "Business"]
    )

    if st.button("Analyze Resume"):
        if resume_text:
            suggestions = resume_analysis(resume_text, interest, goal)

            st.success("Resume Analysis Completed")

            for item in suggestions:
                st.write(f"• {item}")
        else:
            st.warning("Please paste your resume summary first.")


# -----------------------------------
# 6-MONTH ROADMAP
# -----------------------------------
elif menu == "6-Month Roadmap":
    st.subheader("Personalized 6-Month Career Roadmap")

    interest = st.selectbox(
        "Select Your Interest",
        ["Coding", "Electrical", "Biology", "Government Jobs", "Business"]
    )

    goal = st.selectbox(
        "Select Your Goal",
        ["Job", "Higher Studies", "Government Exams", "Business"]
    )

    if st.button("Generate Roadmap"):
        roadmap = generate_roadmap(interest, goal)

        st.success("Your Personalized Career Roadmap")

        for step in roadmap:
            st.write(f"• {step}")


# -----------------------------------
# ADMIN DASHBOARD
# -----------------------------------
elif menu == "Admin Dashboard":
    st.subheader("Admin Dashboard")

    c.execute("""
        SELECT name, percentage, interest, goal, created_at
        FROM users
    """)

    data = c.fetchall()

    if data:
        for row in data:
            st.write(row)
    else:
        st.warning("No student records found.")