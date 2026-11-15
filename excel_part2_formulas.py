EXCEL_PART2_FORMULAS = [
    {
        "case": "Case 2 — Text Extraction",
        "question": "Cell A2 contains JAP1080-19M. Write an Excel formula to extract the first three characters (JAP).",
        "answer": "=LEFT(A2,3)",
        "explanation": "LEFT extracts characters from the beginning of a text string."
    },
    {
        "case": "Case 2 — Text Extraction",
        "question": "Cell A2 contains JAP1080-19M. Write an Excel formula to extract the four-digit employee ID (1080).",
        "answer": "=MID(A2,4,4)",
        "explanation": "MID starts at character 4 and extracts four characters."
    },
    {
        "case": "Case 2 — Text Extraction",
        "question": "Cell A2 contains JAP1080-19M. Write an Excel formula to extract the two-digit code (19) after the hyphen.",
        "answer": "=MID(A2,9,2)",
        "explanation": "MID extracts the two characters immediately after the hyphen."
    },
    {
        "case": "Case 2 — Text Extraction",
        "question": "Cell A2 contains JAP1080-19M. Write an Excel formula to extract the final character (M).",
        "answer": "=RIGHT(A2,1)",
        "explanation": "RIGHT extracts one character from the end of the text string."
    },
    {
        "case": "Case 2 — Text Extraction",
        "question": "Cell A2 contains JAP1080-19M. Write an Excel formula to find the position of the hyphen.",
        "answer": '=FIND("-",A2)',
        "explanation": "FIND returns the position of the hyphen, which is character 8."
    }
]