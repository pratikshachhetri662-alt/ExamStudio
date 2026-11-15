
import streamlit as st

from questions_complete import sql_questions
from excel_questions import excel_questions

st.set_page_config(
    page_title="ExamStudio",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ExamStudio")

st.subheader("Data Analytics in Accounting")

st.write(
    "Welcome to ExamStudio, an interactive learning platform "
    "designed to support exam preparation in Data Analytics in Accounting. "
    "Practise Excel and SQL questions, receive immediate feedback, "
    "and monitor your progress as you develop your analytical skills."
)

st.header("Choose Your Practice Area")
st.caption("Select Excel or SQL below to begin practising. Answer each question, check your response, and use the navigation buttons to continue.")
st.info("Study tip: Review the correct answers and explanations to strengthen your understanding before moving to the next question.")

col1, col2 = st.columns(2)


if "subject" not in st.session_state:
    st.session_state.subject = None

with col1:
    if st.button("📊 Excel Practice"):
        st.session_state.subject = "Excel"

with col2:
    if st.button("🗄️ SQL Practice"):
        st.session_state.subject = "SQL"

if st.session_state.subject:
    st.info(
        f"You selected {st.session_state.subject} Practice!"
    )



if st.session_state.subject == "Excel":
    st.divider()
    st.header("📊 Excel Practice")

    excel_question_index = st.session_state.get("excel_question_index", 0)
    question_number = excel_question_index + 1
    st.progress(question_number / len(excel_questions))
    st.write(f"Question {question_number} of {len(excel_questions)}")
    question = excel_questions[excel_question_index]
    st.subheader(f"Excel Question {question_number}")
    st.write(question["question"])

    user_answer = st.text_input(
    "Type your answer:",
    key=f"excel_answer_{question_number}"
    )

    if st.button("Check Answer", key=f"check_excel_{question_number}"):
        correct_answer = str(question["answer"]).strip().lower()
        submitted_answer = user_answer.strip().lower()

        if not submitted_answer:
            st.warning("Please type an answer first.")
        elif submitted_answer == correct_answer:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is: {question['answer']}")

    st.divider() 
    if st.button("Next Question", disabled=excel_question_index == len(excel_questions) - 1):
        if excel_question_index < len(excel_questions) - 1:
            st.session_state.excel_question_index = excel_question_index + 1
            st.rerun()
    if st.button("Previous Question", disabled=excel_question_index == 0):
        if excel_question_index > 0:
            st.session_state.excel_question_index = excel_question_index - 1
            st.rerun()
if st.session_state.subject == "SQL":
    sql_question_index = st.session_state.get("sql_question_index", 0) 
    st.divider()
    st.header("🗄️ SQL Practice")

    question_number = sql_question_index + 1
    st.progress(question_number / len(sql_questions))
    
    st.write(f"Question {question_number} of {len(sql_questions)}")
    question = sql_questions[sql_question_index]
    
    st.write(question["question"])

    selected_answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"sql_answer_{question_number}",
        index=None,
    )
    if "sql_revision_questions" not in st.session_state:
        st.session_state.sql_revision_questions = []
    if st.button("Check Answer", key=f"check_sql_{question_number}"):
        if selected_answer == question["answer"]:
            st.success("Correct!")
            if question_number in st.session_state.sql_revision_questions:
                st.session_state.sql_revision_questions.remove(question_number)
        else:
            st.error(f"Incorrect. The correct answer is: {question['answer']}")
            if question_number not in st.session_state.sql_revision_questions:
                st.session_state.sql_revision_questions.append(question_number)
            
    if question["explanation"]:
        st.caption(question["explanation"])
    if st.button("Next SQL Question", disabled=sql_question_index == len(sql_questions) - 1):
        if sql_question_index < len(sql_questions) - 1:
            st.session_state.sql_question_index = sql_question_index + 1
            st.rerun()

    if st.button("Previous SQL Question", disabled=sql_question_index == 0):
        if sql_question_index > 0:
            st.session_state.sql_question_index = sql_question_index - 1
            st.rerun()
    st.write("Questions to Revise:", ", ".join(map(str, st.session_state.sql_revision_questions)) or "None yet")
    if st.button("Revise My Mistakes"):
        if st.session_state.sql_revision_questions:
            st.session_state.sql_question_index = st.session_state.sql_revision_questions[0] - 1
            st.rerun()
        else:
            st.info("No incorrect questions to revise yet!") 
st.divider()
st.caption("ExamStudio | Data Analytics in Accounting | Educational Practice Platform")