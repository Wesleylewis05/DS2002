import pandas as pd

best_m_by_year = pd.read_csv(f"Best Movie by Year Netflix.csv").drop(columns=["MAIN_PRODUCTION"])
best_m_overall =pd.read_csv(f"Best Movies Netflix.csv").drop(columns=["NUMBER_OF_VOTES","DURATION","MAIN_PRODUCTION"])
best_s_by_year = pd.read_csv(f"Best Show by Year Netflix.csv").drop(columns=["NUMBER_OF_SEASONS","MAIN_PRODUCTION"])
best_s_overall = pd.read_csv(f"Best Shows Netflix.csv").drop(columns=["NUMBER_OF_VOTES","DURATION","NUMBER_OF_SEASONS","MAIN_PRODUCTION"])
raw_credits = pd.read_csv(f"raw_credits.csv")
raw_titles = pd.read_csv(f"raw_titles.csv")

"""
Part 1 will be to extract these data sources into one Pandas. Note to only extract the data that supports
the types of questions you want. This is the Extract and Transform sections. For example, if you choose
not to allow users to ask about the number of seasons, do not extract that into your new data set.
"""

print(best_m_by_year)
print(best_m_overall)
print(best_s_by_year)
print(best_s_overall)
print(raw_credits)
print(raw_titles)
