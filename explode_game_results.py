import pandas as pd
import ast

df = pd.read_csv("game_results.csv")

def parse_letters(val):
    try:
        return ast.literal_eval(val)
    except:
        return []

df["wrong_letters"] = df["wrong_letters"].apply(parse_letters)
exploded = df.explode("wrong_letters")
exploded["wrong_letters"] = exploded["wrong_letters"].str.strip()
exploded.to_csv("game_results_exploded.csv", index=False)
print("Done!", len(exploded), "rows")