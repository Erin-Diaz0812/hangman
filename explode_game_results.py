import pandas as pd
import ast

df = pd.read_csv("game_results.csv")

def parse_letters(val):
    try:
        return ast.literal_eval(val)
    except:
        return []

df["wrong_letter"] = df["Wrong Letters"].apply(parse_letters)
exploded = df.explode("wrong_letter")
exploded["wrong_letter"] = exploded["wrong_letter"].str.strip()
exploded.to_csv("game_results_exploded.csv", index=False)
print("Done!", len(exploded), "rows")