import streamlit as st

# Page config
st.set_page_config(page_title="Ahmed Nadeem's Resume", layout="centered")

# Profile picture
st.image("Public/Profile.jpg", width=200)

# Name and title
st.title("Ahmed Nadeem")
st.subheader("Beginner Python Developer | Commerce Student")

# Contact Info Section
st.markdown(f"""
### 🔗 Contact Me

📧 **Email:** ahmednadeem0004@gmail.com <br>
📱 **Phone:** +92 318 2686893 <br>
🌐 [GitHub](https://github.com/MrAhmed42) | [LinkedIn](https://www.linkedin.com/in/ahmednadeem42)
""", unsafe_allow_html=True)

# Objective
st.markdown("### 🎯 Career Objective")
st.write("""
Motivated beginner Python developer with a strong foundation in commerce, eager to apply both technical 
and business knowledge to real-world projects, grow as a developer, and contribute effectively to team goals.
""")

# Education
st.markdown("### 🎓 Education")
st.write("**Intermediate in Commerce** – G.C.C.E College – Karachi Board *(Completed 1st Year with 73%; 2nd Year in Progress)*")
st.write("**Matriculation – General Group** – Tayab Ali A. Alavi Boys Secondary School – Karachi Board *(72%)*")

# Skills
st.markdown("### 🛠 Skills")
st.write("""
- Python (Control Flow, Functions, Data Types, Exception Handling)
- Google Colab, Jupyter Notebook
- Streamlit (Beginner Level)
- Git & GitHub (Basics)
""")

# Currently Learning
st.markdown("### 📘 Currently Learning")
st.write("Python programming through the **GIAIC (Governor Initiative for AI & Computing)** program *(ongoing)*")

# Projects
st.markdown("### 📁 Projects")
st.write("""
- Developed **15+ Python console-based projects**, including:
    - Mad Libs Story Generator
    - Number Guessing Games (User and Computer modes)
    - Rock-Paper-Scissors
    - Hangman
    - Countdown Timer
    - Password Generator
    - Quiz App
    - Simple Calculator
- Created web-based apps with **Streamlit**:
    - BMI Calculator
    - Interactive Resume App (this one!)
- [🔗 View complete project portfolio on GitHub](https://github.com/MrAhmed42)
""")

# Footer
st.markdown("---")
st.caption("This resume was built using Python and Streamlit.")
