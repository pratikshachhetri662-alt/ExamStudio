
EXCEL_PART4_QUESTIONS = [
    {
        "question": "What is the main business objective of the restaurant case?",
        "answer": "Predict total restaurant sales 7 days after the last date in the dataset",
        "explanation": "Bob needs a seven-day-ahead sales forecast to plan ingredient purchases and employee shifts."
    },
    {
        "question": "Which field in salesData represents before-tax sales revenue for a menu item on a given day?",
        "answer": "netTotal",
        "explanation": "The data dictionary defines netTotal as the before-tax dollars received for a menu item during the day."
    },
    {
        "question": "Which field should be used to merge salesData with weatherData?",
        "answer": "date",
        "explanation": "Both datasets contain a date field, allowing sales and weather observations to be matched by calendar day."
    },
    {
        "question": "Which Excel operation can aggregate menu-item revenue into total daily sales?",
        "answer": "SUMIFS",
        "explanation": "SUMIFS can sum netTotal for all menu items sharing the same date. A PivotTable is another valid method."
    },
    {
        "question": "What should the dependent variable be when predicting total daily restaurant sales?",
        "answer": "Total daily sales",
        "explanation": "The dependent variable is the outcome being predicted. Daily sales should be aggregated across menu items."
    },
    {
        "question": "Which weatherData field represents the daily maximum temperature?",
        "answer": "tmax",
        "explanation": "The weather data dictionary defines tmax as maximum daily temperature in Fahrenheit."
    },
    {
        "question": "Which weatherData field represents the daily minimum temperature?",
        "answer": "tmin",
        "explanation": "The weather data dictionary defines tmin as minimum daily temperature in Fahrenheit."
    },
    {
        "question": "Which gameData variable indicates whether a football game occurred on a date?",
        "answer": "gameDay",
        "explanation": "gameDay equals 1 when a game occurred and 0 otherwise."
    },
    {
        "question": "Which gameData variable specifically indicates a home football game?",
        "answer": "homeGame",
        "explanation": "homeGame equals 1 when the game was played at home and 0 otherwise."
    },
    {
        "question": "Which salesData variable represents revenue for a menu item 364 days earlier?",
        "answer": "netTotal_364",
        "explanation": "The suffix _364 refers to 364 days earlier, approximately the same weekday in the previous year."
    },
    {
        "question": "In a regression of daily sales on temperature, what does a positive temperature coefficient indicate?",
        "answer": "Higher predicted sales",
        "explanation": "A positive coefficient means higher temperature is associated with higher predicted sales, holding other included variables constant."
    },
    {
        "question": "What does a negative coefficient for gameDay indicate in a regression predicting sales?",
        "answer": "Lower predicted sales on game days",
        "explanation": "A negative gameDay coefficient indicates lower predicted sales on game days than non-game days, holding other included variables constant."
    },
    {
        "question": "What is the purpose of including an interaction between previous-year sales and gameDay?",
        "answer": "Test whether the relationship between previous-year sales and current sales differs on game days",
        "explanation": "An interaction term allows the association between previous-year sales and current sales to vary depending on gameDay."
    },
    {
        "question": "If a regression coefficient has a p-value of 0.03, is it statistically significant at the 5% level?",
        "answer": "Yes",
        "explanation": "A p-value of 0.03 is below 0.05. Statistical significance alone does not establish causation."
    },
    {
        "question": "What is one important limitation to explain when communicating a sales forecast to Bob?",
        "answer": "Prediction uncertainty",
        "explanation": "Bob should understand that predicted sales are estimates and may differ from actual sales. A prediction interval can help communicate uncertainty."
    },
    {
        "question": "Why should gameData be merged carefully with the daily sales dataset?",
        "answer": "Dates without games may not appear in gameData",
        "explanation": "The game dataset lists game dates. A careful merge must preserve non-game sales dates and correctly represent their game-day status."
    }
]
