
SQL_PART2_QUESTIONS = [
    {
        "question": "Task 4, Q1: Which SQL keyword sorts transaction amounts from highest to lowest?",
        "answer": "DESC",
        "explanation": "Use ORDER BY Amount DESC to display the most expensive transactions first."
    },
    {
        "question": "Task 4, Q2: What SQL condition selects only transactions from calendar year 2014?",
        "answer": "Year = 2014",
        "explanation": "The supplied database has a Year column. Use WHERE Year = 2014, then ORDER BY Month ASC, Amount DESC, FullName ASC."
    },
    {
        "question": "Task 4, Q3: What SQL condition selects transactions greater than $3,000?",
        "answer": "Amount > 3000",
        "explanation": "Use WHERE Year = 2014 AND Amount > 3000. The > operator excludes transactions equal to $3,000."
    },
    {
        "question": "Task 4, Q4: Complete the condition for vendors containing Amazon: Vendor LIKE ____",
        "answer": "'%Amazon%'",
        "explanation": "The % wildcard matches any sequence of characters. Vendor LIKE '%Amazon%' finds names containing Amazon."
    },
    {
        "question": "Task 4, Q5: Which SQL aggregate function counts all transaction rows?",
        "answer": "COUNT(*)",
        "explanation": "SELECT COUNT(*) AS TotalTrans FROM pcards counts all rows, including rows with NULL values in individual columns."
    },
    {
        "question": "Task 4, Q6: Which comparison operator includes transactions equal to or greater than $5,000?",
        "answer": ">=",
        "explanation": "Use WHERE Amount >= 5000. Unlike >, this includes transactions of exactly $5,000."
    },
    {
        "question": "Task 4, Q7: Are refunds represented by positive or negative amounts in the P-card database?",
        "answer": "Negative",
        "explanation": "Returns and refunds have negative Amount values. For January–March 2014, filter Year = 2014, Month BETWEEN 1 AND 3, and Amount < 0."
    },
    {
        "question": "Task 4, Q8: Which SQL clause groups transaction counts by year?",
        "answer": "GROUP BY",
        "explanation": "Use SELECT Year, COUNT(*) AS TotalTrans FROM pcards GROUP BY Year ORDER BY Year DESC."
    },
    {
        "question": "Task 4, Q9: Which aggregate function counts the transactions made by each cardholder?",
        "answer": "COUNT(*)",
        "explanation": "Filter Year = 2014, GROUP BY FullName, and ORDER BY COUNT(*) DESC to rank cardholders by transaction count."
    },
    {
        "question": "Task 4, Q10: Should returned transactions be selected using Amount < 0 or Amount > 0?",
        "answer": "Amount < 0",
        "explanation": "Refunds are negative. Group 2014 returns by FullName and calculate SUM(Amount) and COUNT(*). The most negative sum represents the greatest refund value."
    },
    {
        "question": "Task 4, Q11: Which SQL clause filters grouped cardholders to those with more than 10 transactions?",
        "answer": "HAVING",
        "explanation": "Use GROUP BY FullName HAVING COUNT(*) > 10. HAVING filters groups after aggregation; WHERE filters individual rows before aggregation."
    },
    {
        "question": "Task 4, Q12: Which SQL clause filters cardholders whose total returned goods exceed $1,000?",
        "answer": "HAVING",
        "explanation": "After filtering Amount < 0 and grouping by FullName, use HAVING SUM(Amount) < -1000. Refunds are stored as negative amounts."
    },
    {
        "question": "Task 5: What is the maximum single-transaction P-card limit stated in the OSU guidelines, in dollars?",
        "answer": "5000",
        "explanation": "The case guidelines state a maximum single-transaction limit of $5,000, including applicable shipping and handling charges."
    },
    {
        "question": "Task 5: What annual spending threshold, in dollars, is used in the first internal-control test?",
        "answer": "50000",
        "explanation": "Task 5, Question 1 asks auditors to identify employees whose total 2014 spending exceeds $50,000."
    },
    {
        "question": "Task 5: What monthly spending threshold, in dollars, is examined for spending without approval?",
        "answer": "10000",
        "explanation": "Task 5, Question 2 asks auditors to identify employees spending more than $10,000 in a month. Approval information is needed before concluding a violation occurred."
    },
    {
        "question": "Audit interpretation: Does a flagged suspicious transaction automatically prove fraud? Answer Yes or No.",
        "answer": "No",
        "explanation": "An unusual transaction is an indicator for further audit investigation, not proof of fraud or misconduct."
    }
]
