import sys
import wikipedia
import numpy as np
import pandas as pd
import nltk

from src.logger import logging
from src.exception import CustomException

# Geting data from wikipedia
def get_data(search_query):
    try:
        summary = wikipedia.summary(search_query)
        return summary
    except Exception as e:
        logging.info(f"Error occured while fetching data from wikipedia: {e}")
        raise CustomException(e, sys)

data = []
def get_sententces(content):
    nltk.download('punkt')
    try:
        sentences = nltk.sent_tokenize(content)
        for sentence in sentences:
            data.append(sentence.strip())
    except Exception as e:
        logging.info(f"Error occured while getting sentences from conents: {e}")
        raise CustomException(e, sys)

def convert_data_to_df(data: list) -> pd.DataFrame:
    try:
        df = pd.DataFrame({'sentence': data})
        return df
    except Exception as e:
        logging.info(f"Error occured while converting data to dataframe: {e}")
        raise CustomException(e, sys)

def save_df_to_csv(df: pd.DataFrame, path: str):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        logging.info(f"Error occured while saving dataframe to csv: {e}")
        raise CustomException(e, sys)



if __name__ == "__main__":
    content = get_data("Visual_Studio_Code")
    get_sententces(content)
    df = pd.read_csv("data/data.csv")
    new_df = convert_data_to_df(data)
    df = pd.concat([df, new_df])
    save_df_to_csv(df, "data/data.csv")
    


# summary = wikipedia.summary("Python (programming language)")


# print(summary)
# # fetch_data.py