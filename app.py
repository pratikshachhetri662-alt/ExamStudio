
import streamlit as st

from questions_complete import sql_questions
from excel_questions import excel_questions
from excel_part2_questions import EXCEL_PART2_QUESTIONS
from excel_part2_formulas import EXCEL_PART2_FORMULAS
from excel_part3_questions_generated import EXCEL_PART3_QUESTIONS
from excel_part4_questions import EXCEL_PART4_QUESTIONS
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

col1, col2, col3, col4, col5 = st.columns(5)


if "subject" not in st.session_state:
    st.session_state.subject = None

with col1:
    if st.button("📊 Excel Practice"):
        st.session_state.subject = "Excel"

with col2:
    if st.button("🗄️ SQL Practice"):
        st.session_state.subject = "SQL"
with col3:
    if st.button("📘 Excel Part 2 — ETL"):
        st.session_state.subject = "Excel Part 2"
with col4:
    if st.button("📈 Excel Part 3 — IntegrateCo"):
        st.session_state.subject = "Excel Part 3"
with col5:
    if st.button("🍽️ Excel Part 4 — Restaurant"):
        st.session_state.subject = "Excel Part 4"  
if st.session_state.subject:
    st.info(
        f"You selected {st.session_state.subject} Practice!"
    )



if st.session_state.subject == "Excel":
    st.divider()
    st.header("📊 Excel Practice")
    if "excel_mistakes" not in st.session_state:
        st.session_state.excel_mistakes = []
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
            if question_number in st.session_state.excel_mistakes:
                st.session_state.excel_mistakes.remove(question_number)

        else:
            st.error(f"Incorrect. The correct answer is: {question['answer']}")
            if question_number not in st.session_state.excel_mistakes:
                st.session_state.excel_mistakes.append(question_number)
    if st.session_state.excel_mistakes:
        st.write("Questions to Revise:", ", ".join(map(str, sorted(st.session_state.excel_mistakes))))
    st.divider() 
    if st.button("Next Question", disabled=excel_question_index == len(excel_questions) - 1):
        if excel_question_index < len(excel_questions) - 1:
            st.session_state.excel_question_index = excel_question_index + 1
            st.rerun()
    if st.button("Previous Question", disabled=excel_question_index == 0):
        if excel_question_index > 0:
            st.session_state.excel_question_index = excel_question_index - 1
            st.rerun()
    if st.session_state.excel_mistakes:
        if st.button("Revise My Mistakes", key="revise_excel"):
            st.session_state.excel_question_index = min(st.session_state.excel_mistakes) - 1
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
if st.session_state.subject == "Excel Part 2":
    st.divider()
    st.header("📘 Excel Part 2 — ETL Case Studies")

    if "etl_index" not in st.session_state:
        st.session_state.etl_index = 0

    if "etl_mistakes" not in st.session_state:
        st.session_state.etl_mistakes = []

    index = st.session_state.etl_index
    question = EXCEL_PART2_QUESTIONS[index]
    number = index + 1

    st.progress(number / len(EXCEL_PART2_QUESTIONS))
    st.write(f"Question {number} of {len(EXCEL_PART2_QUESTIONS)}")
    st.caption(question["case"])
    st.subheader(question["question"])

    answer = st.radio(
        "Choose your answer:",
        question["options"],
        index=None,
        key=f"etl_answer_{number}"
    )

    if st.button("Check ETL Answer", key=f"check_etl_{number}"):
        if answer is None:
            st.warning("Please select an answer first.")
        elif answer == question["answer"]:
            st.success("Correct!")
            if number in st.session_state.etl_mistakes:
                st.session_state.etl_mistakes.remove(number)
        else:
            st.error(f"Incorrect. Correct answer: {question['answer']}")
            if number not in st.session_state.etl_mistakes:
                st.session_state.etl_mistakes.append(number)

        if answer is not None:
            st.info(question["explanation"])

    col_prev, col_next = st.columns(2)

    with col_prev:
        if st.button("Previous ETL Question", disabled=index == 0):
            st.session_state.etl_index -= 1
            st.rerun()

    with col_next:
        if st.button(
            "Next ETL Question",
            disabled=index == len(EXCEL_PART2_QUESTIONS) - 1
        ):
            st.session_state.etl_index += 1
            st.rerun()

    st.write(
        "Questions to Revise:",
        ", ".join(map(str, sorted(st.session_state.etl_mistakes)))
        or "None yet"
    )

    if st.button("Revise My ETL Mistakes"):
        if st.session_state.etl_mistakes:
            st.session_state.etl_index = min(st.session_state.etl_mistakes) - 1
            st.rerun()
        else:
            st.info("No incorrect questions to revise!")
if st.session_state.subject == "Excel Part 2":
    st.divider()
    st.header("✍️ Practical Excel Formula Exercises")

    if "formula_index" not in st.session_state:
        st.session_state.formula_index = 0

    index = st.session_state.formula_index
    question = EXCEL_PART2_FORMULAS[index]

    st.write(
        f"Formula Question {index + 1} of {len(EXCEL_PART2_FORMULAS)}"
    )
    st.write(question["question"])

    user_formula = st.text_input(
        "Type your Excel formula:",
        key=f"formula_answer_{index}"
    )

    if st.button("Check Formula"):
        submitted = user_formula.strip().replace(" ", "").upper()
        expected = question["answer"].strip().replace(" ", "").upper()

        if not submitted:
            st.warning("Please enter a formula.")
        elif submitted == expected:
            st.success("Correct!")
            st.info(question["explanation"])
        else:
            st.error(f"Expected formula: {question['answer']}")
            st.info(question["explanation"])

    if st.button(
        "Next Formula Question",
        disabled=index == len(EXCEL_PART2_FORMULAS) - 1
    ):
        st.session_state.formula_index += 1
        st.rerun()

    if st.button(
        "Previous Formula Question",
        disabled=index == 0
    ):
        st.session_state.formula_index -= 1
        st.rerun()
if st.session_state.subject == "Excel Part 3":
    st.divider()
    st.header("📈 Excel Part 3 — IntegrateCo")

    if "part3_index" not in st.session_state:
        st.session_state.part3_index = 0
    if "part3_mistakes" not in st.session_state:
        st.session_state.part3_mistakes = []
    index = st.session_state.part3_index
    question = EXCEL_PART3_QUESTIONS[index]

    st.progress((index + 1) / len(EXCEL_PART3_QUESTIONS))
    st.write(f"Question {index + 1} of {len(EXCEL_PART3_QUESTIONS)}")
    st.write(question["question"])

    user_answer = st.text_input(
        "Your answer:",
        key=f"part3_answer_{index}"
    )

    if st.button("Check Part 3 Answer"):
        submitted = user_answer.strip().lower().replace(",", "")
        expected = str(question["answer"]).strip().lower().replace(",", "")

        if not submitted:
            st.warning("Please enter an answer.")

        elif submitted == expected:
            st.success("Correct!")
            st.info(question["explanation"])

            if index + 1 in st.session_state.part3_mistakes:
                st.session_state.part3_mistakes.remove(index + 1)

        else:
            st.error(f"Incorrect. Correct answer: {question['answer']}")
            st.info(question["explanation"])

            if index + 1 not in st.session_state.part3_mistakes:
                st.session_state.part3_mistakes.append(index + 1)

    col_previous, col_next = st.columns(2)

    with col_previous:
        if st.button("Previous Part 3 Question", disabled=index == 0):
            st.session_state.part3_index -= 1
            st.rerun()

    with col_next:
        if st.button(
            "Next Part 3 Question",
            disabled=index == len(EXCEL_PART3_QUESTIONS) - 1
        ):
            st.session_state.part3_index += 1
            st.rerun()
    st.write(
        "Questions to Revise:",
        ", ".join(map(str, sorted(st.session_state.part3_mistakes)))
        or "None yet"
    )

    if st.button("🔄 Revise My Part 3 Mistakes"):
        if st.session_state.part3_mistakes:
            st.session_state.part3_index = min(
                st.session_state.part3_mistakes
            ) - 1
            st.rerun()
        else:
            st.info("No incorrect questions to revise!")

# Excel Part 4 — Restaurant Sales Forecasting
if st.session_state.subject == "Excel Part 4":

    st.header("🍽️ Excel Part 4 — Restaurant Sales Forecasting")

    if "part4_index" not in st.session_state:
        st.session_state.part4_index = 0
    if "part4_mistakes" not in st.session_state:
        st.session_state.part4_mistakes = []
    index = st.session_state.part4_index
    question = EXCEL_PART4_QUESTIONS[index]

    st.write(f"Question {index + 1} of {len(EXCEL_PART4_QUESTIONS)}")
    st.progress((index + 1) / len(EXCEL_PART4_QUESTIONS))
    st.write(question["question"])

    user_answer = st.text_input(
        "Your answer:",
        key=f"part4_answer_{index}"
    )

    
    if st.button("Check Part 4 Answer"):
        submitted = user_answer.strip().lower()
        expected = str(question["answer"]).strip().lower()

        if not submitted:
            st.warning("Please enter an answer.")

        elif submitted == expected:
            st.success("Correct!")
            st.info(question["explanation"])

            if index + 1 in st.session_state.part4_mistakes:
                st.session_state.part4_mistakes.remove(index + 1)

        else:
            st.error(f"Incorrect. Suggested answer: {question['answer']}")
            st.info(question["explanation"])

            if index + 1 not in st.session_state.part4_mistakes:
                st.session_state.part4_mistakes.append(index + 1)

   
    col_previous4, col_next4 = st.columns(2)

    with col_previous4:
        if st.button(
            "⬅️ Previous Part 4 Question",
            disabled=(index == 0)
        ):
            st.session_state.part4_index -= 1
            st.rerun()

    with col_next4:
        if st.button(
            "Next Part 4 Question ➡️",
            disabled=(index == len(EXCEL_PART4_QUESTIONS) - 1)
        ):
            st.session_state.part4_index += 1
            st.rerun()


    st.write(
        "Questions to Revise:",
        ", ".join(map(str, sorted(st.session_state.part4_mistakes)))
        or "None yet"
    )

    if st.button("🔄 Revise My Part 4 Mistakes"):
        if st.session_state.part4_mistakes:
            st.session_state.part4_index = min(
                st.session_state.part4_mistakes
            ) - 1
            st.rerun()
        else:
            st.info("No incorrect questions to revise!")

st.divider()
st.caption("ExamStudio | Data Analytics in Accounting | Educational Practice Platform")